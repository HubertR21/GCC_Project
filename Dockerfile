FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY ["DEV.py", "requirements.txt", "main.py", "index.pkl", "filenames.txt", "./"] .
COPY ./static/styles.css ./static/styles.css
COPY ./templates/images.html ./templates/images.html
COPY ./templates/index.html ./templates/index.html
RUN pip install -r requirements.txt
# Expose the app port
EXPOSE 80

# Run command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]