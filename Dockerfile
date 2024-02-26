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
