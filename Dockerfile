# Use an official Python runtime as a parent image
FROM python:3.7-slim

EXPOSE 8000
WORKDIR /app 
COPY . /app 
RUN pip3 install -r requirements.txt --no-cache-dir
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]