# Use an official Python runtime as a pImproved data handling in FixtureCollection, LeagueTable, and ZPNs: updated network settings, enhanced JSON output, and ensured proper string handlingarent image
FROM python:3.12

ENV PYTHONUNBUFFERED 1

# Copy the current directory to /app in the container
COPY . /app

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the PYTHONPATH environment variable so Python can see the scraper module
ENV PYTHONPATH=/app

CMD ["python","API/manage.py","runserver","8001"]