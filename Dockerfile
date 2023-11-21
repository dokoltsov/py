# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy app code to the container
COPY ./app /app
COPY ./requirements.txt /app

# Install dependencies
RUN pip install -r /app/requirements.txt

# Expose port 8080 for the Flask app
EXPOSE 8080

# Set the command to start the Flask app when container starts
CMD ["python", "/app/main.py"]