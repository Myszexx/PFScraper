# Use an official Python runtime as a parent image
FROM python:3.12

ENV PYTHONUNBUFFERED 1

# Copy the current directory to /app in the container
COPY . /app

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the PYTHONPATH environment variable so Python can see the scraper module
ENV PYTHONPATH=/app

CMD ["python","manage.py","runserver","8001"]