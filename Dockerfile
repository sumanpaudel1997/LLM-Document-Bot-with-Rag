# Use the official Python base image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED=1
ARG OPENAI_API_KEY=$OPENAI_API_KEY

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Specify the command to run your Python app
CMD ["python3", "main.py"]
