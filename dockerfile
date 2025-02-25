# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to the /app directory inside the Docker image
COPY requirements.txt /app/requirements.txt

# Install the required packages
RUN pip install -r /app/requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Command to run your application
CMD ["python", "app.py"]
