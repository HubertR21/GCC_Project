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
- docker tag default-service-fastpai:latest europe-west2-docker.pkg.dev/fast-api-gcc/repo/default-service-fastpai:latest
- docker push europe-west2-docker.pkg.dev/fast-api-gcc/repo/default-service-fastpai:latest
