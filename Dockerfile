# Use an official Python runtime as a parent image
FROM python:3.9-slim


ENV PYTHONUNBUFFERED 1
# Skopiuj bieżący katalog do /app w kontenerze
COPY . /app

# Ustaw katalog roboczy
WORKDIR /app

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Ustaw zmienną środowiskową PYTHONPATH, aby Python widział moduł scraper
ENV PYTHONPATH=/app

# Udostępnij port 50051
EXPOSE 50051

# Uruchom serwer gRPC
CMD ["python", "/scraper/core/scraper_server.py"]

