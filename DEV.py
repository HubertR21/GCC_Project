import clip
import torch
import requests
from PIL import Image
from io import BytesIO
import faiss
import pickle

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

d = 512
index = faiss.IndexFlatIP(d)

with open('filenames.txt','r') as f:
    filenames = f.readlines()
    f.close()

for filename in filenames:
    url = "https://storage.googleapis.com/images_gcc2023/train2017/"+filename[:-1]
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    image = preprocess(img).unsqueeze(0).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        index.add(image_features)
        if index.ntotal%100==0:
            print(index.ntotal)


file = open('index.pkl',"wb")
pickle.dump(index,file)
file.close()