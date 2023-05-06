FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY ["DEV.py", "requirements.txt", "main.py", "filenames.txt", "./"] .
COPY ./static/styles.css ./static/styles.css
COPY ./templates/images.html ./templates/images.html
COPY ./templates/index.html ./templates/index.html

RUN python -m venv env
RUN . env/bin/activate
RUN pip install -r requirements.txt