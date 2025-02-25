# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY . .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy project files to the working directory
COPY . .

# Command to run the application
CMD ["python", "app.py"]
