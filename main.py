from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("index.html", context)


@app.post('/', response_class=HTMLResponse)
async def index(request: Request, image: UploadFile = File(...)):
    form_data = await request.form()
    context = {'request': request,'urls':['https://upload.wikimedia.org/wikipedia/commons/1/15/Cat_August_2010-4.jpg','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSM1cDnT1Q5ZrkfLfxiSgFvC2ZsjpngynJGvg&usqp=CAU']*5}
    if form_data['image'].file.read()!=bytes(0):
        pil_image = Image.open(image.file) # HERE IS THE IMAGE

    else:
        text = form_data["text_input"] # HERE IS THE TEXT (TEXT CAN BE URL?)

    return templates.TemplateResponse("images.html", context)