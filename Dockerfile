# Use the official Python 3.11 Alpine image as a parent image
FROM --platform=linux/amd64 python:3.11-alpine

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the necessary ports (if required)
EXPOSE 8000
EXPOSE 5432

# Define the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]