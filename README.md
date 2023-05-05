# GCC_Project
Google Cloud project for Cloud Computing classes on MiNI, WUT

- Download photos from COCO (https://cocodataset.org/#home)
- Upload photos to Cloud (accessible via URL, in the public folder)
- ~~Transform photos to vectors (csv with mapping index - url, vectors held in faiss)~~

- Create a VM
- Upload an app (frontend, api calls, model) to Docker
- Opening the ports and netowrking

# Odpalanie dockera
- docker build
- docker build -t default-service-fastpai:latest .
- docker tag default-service-fastpai:latest europe-west2-docker.pkg.dev/gcc2023-385607/repo/default-service-fastpai:latest
- docker push europe-west2-docker.pkg.dev/gcc2023-385607/repo/default-service-fastpai:latest


# Description

## Functionality

This app allows uploading an image or the text, and then uses a CLIP (Contrastive Language-Image Pre-Training) neural network to browse our selection of thousands of photos to find pictures that are similar to the uploaded file or the provided image description. The application suggests dozens of answers which have the highest similarity score to the input.

## UI

The UI is a static web page hosted on the Google Cloud Container. The minimalistic interface is written in the HTML and CSS only, without using any advances languages or engines. The interfeace also presents photos selected by the machine learning model in the form of url images. 

## Storage

The images are present inside of the Google Cloud Storage and all of them are available from the internet. Rest of the files are present in the Docker Container, including the CLIP model,  `index.pkl` file (which holds the images and texts from the database vectorized by CLIP and saved by faiss), and the `filenames.txt` which includes the images names.

## Processing
