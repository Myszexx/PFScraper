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

# Expose port 50051
EXPOSE 50051

# Run the gRPC server
CMD ["python", "scraper/core/scraper_server.py"]