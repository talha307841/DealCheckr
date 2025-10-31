FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app ./app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
FROM python:3.12-slim

# Production Dockerfile for FastAPI
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
		build-essential \
		gcc \
		libpq-dev \
	&& rm -rf /var/lib/apt/lists/*

# install pip dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy code
COPY app ./app

EXPOSE 8000

# Use uvicorn with sensible default workers for production
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]