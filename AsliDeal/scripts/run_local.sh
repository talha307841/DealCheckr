#!/bin/bash

# This script sets up the local development environment for AsliDeal
# and runs the FastAPI backend and Chrome extension.

# Navigate to the backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Run the FastAPI application
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload &

# Navigate to the Chrome extension directory
cd ../chrome-extension

# Install Node.js dependencies
npm install

# Build the Chrome extension
npm run build

# Open the Chrome extension in the browser
"$BROWSER" "chrome-extension://<your-extension-id>/popup.html"