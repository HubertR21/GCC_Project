from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
from fastapi.staticfiles import StaticFiles
import clip
import torch
import pickle
import numpy as np

storage_url = "https://storage.googleapis.com/images_gcc2023/train2017/"
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)
index = pickle.load(open('index.pkl',"rb"))
with open('filenames.txt','r') as f:
    filenames = f.readlines()
    f.close()

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/', response_class=HTMLResponse)
async def clip_search(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("index.html", context)

@app.post('/', response_class=HTMLResponse)
async def clip_search(request: Request, image: UploadFile = File(...)):
    form_data = await request.form()
    if form_data['image'].file.read()!=bytes(0):
        pil_image = Image.open(image.file)
        image = preprocess(pil_image).unsqueeze(0).to(device)
        with torch.no_grad():
            image_features = model.encode_image(image)
            image_features /= image_features.norm(dim=-1, keepdim=True)
            D, I = index.search(image_features, 20)
            urls = list(map(lambda x: storage_url+x[:-1],np.array(filenames)[I[0]]))
            D=np.round(D*100,2)
        context = {'request': request,'urls':zip(urls,D[0])}
    else:
        text = form_data["text_input"]
        with torch.no_grad():
            text_features = model.encode_text(clip.tokenize([text]).to(device))
            text_features /= text_features.norm(dim=-1, keepdim=True)
            D, I = index.search(text_features, 20)
            urls = list(map(lambda x: storage_url+x[:-1],np.array(filenames)[I[0]]))
            D=np.round(D*100,2)
        context = {'request': request,'urls':zip(urls,D[0])}
    return templates.TemplateResponse("images.html", context)
