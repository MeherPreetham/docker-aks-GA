# Dockerfile

# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/requirements.txt

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Install the required packages
RUN pip install -r /app/requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app

# Command to run the application
CMD ["python", "app.py"]
