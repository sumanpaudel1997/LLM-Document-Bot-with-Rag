# # Use the official Python base image
# FROM python:3.8-slim-buster

# # Set environment variables
# ENV PYTHONUNBUFFERED=1

# ARG OPENAI_API_KEY
# ENV OPENAI_API_KEY=$OPENAI_API_KEY

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the requirements file into the container
# COPY requirements.txt requirements.txt

# # Install the Python dependencies
# RUN RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code into the container
# COPY . .

# # Specify the command to run your Python app
# CMD ["python3", "main.py"]


# Stage 1: Build the application
FROM python:3.8-slim-buster AS builder

# Set working directory
WORKDIR /app

# Copy only requirements.txt to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Stage 2: Create the final image
FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

# Copy the rest of the application code from the builder stage
COPY --from=builder /app .

# Set the OpenAI API key as an environment variable
ARG OPENAI_API_KEY
ENV OPENAI_API_KEY=$OPENAI_API_KEY

# Expose any necessary ports
# EXPOSE 8000

# Command to run the application
CMD ["python", "your_script.py"]
