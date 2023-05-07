# Description

## Functionality

This app allows uploading an image or the text, and then uses a CLIP (Contrastive Language-Image Pre-Training) neural network to browse our selection of thousands of photos to find pictures that are similar to the uploaded file or the provided image description. The application suggests dozens of answers which have the highest similarity score to the input.

## UI

The UI is a dynamic web page hosted on the [Google Cloud Container](https://cloud.google.com/compute/docs/containers). The content of web pages won't always remain the same for all users, as we use the API and the model to change the content of the webpage.

## Storage

The images are present inside of the [Google Cloud Storage](https://cloud.google.com/storage) and all of them are available from the internet. The images are the subset of the [COCO Dataset] (https://cocodataset.org/#download). Rest of the files are present in the Docker Container, including the CLIP model,  `index.pkl` file (which holds the images and texts from the database vectorized by CLIP and saved by faiss), and the `filenames.txt` which includes the images names.

## Processing

The OpenAI [CLIP](https://github.com/openai/CLIP) is dockerized with the rest of the application (hidden data + frontend) and deployed using [Cloud Run](https://cloud.google.com/run). The application is purely asynchronous as for the communication with the model and calling the images we are using a FastAPI.

The [FastAPI](https://fastapi.tiangolo.com) is built on top of the ASGI (Asynchronous Server Gateway Interface) framework, which is designed to handle asynchronous code efficiently. Moreover it uses the async/await syntax to define asynchronous endpoints and functions.

CLIP (Contrastive Language-Image Pre-Training) is a neural network trained on a variety of (image, text) pairs. It can be instructed in natural language to predict the most relevant text snippet, given an image, without directly optimizing for the task, similarly to the zero-shot capabilities of GPT-2 and 3. The CLIP matches the performance of the original ResNet50 on ImageNet “zero-shot” without using any of the original 1.28M labeled examples, overcoming several major challenges in computer vision. The model:
- Given a batch of images, returns the image features encoded by the vision portion of the CLIP model,
- Given a batch of text tokens, returns the text features encoded by the language portion of the CLIP model,
- Given a batch of images and a batch of text tokens, returns two Tensors, containing the logit scores corresponding to each image and text input. The values are cosine similarities between the corresponding image and text features, times 100.
