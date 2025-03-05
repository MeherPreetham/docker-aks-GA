# Dockerfile

# Use the official Python image from the Docker Hub
FROM ubuntu:22.04 AS base

# Set the working directory
WORKDIR / app
#install Python 3.10 and other dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and setuptools
RUN python3.10 -m pip install --upgrade pip setuptools

# Copy the requirements file to the working directory
COPY requirements.txt /app/requirements.txt

# Install the required packages
RUN python3.10 -m pip install -r /app/requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app

# Command to run the application
CMD ["python3", "GAIslandapproach.py"]
