# AsliDeal

AsliDeal is a full-stack application designed to verify discount offers on Pakistani e-commerce sites. The project consists of a Chrome extension that interacts with a FastAPI backend to provide users with reliable information about discounts and offers.

## Project Structure

```
AsliDeal
├── chrome-extension
│   ├── manifest.json
│   ├── src
│   │   ├── background.ts
│   │   ├── content_script.ts
│   │   ├── popup
│   │   │   ├── popup.html
│   │   │   ├── popup.ts
│   │   │   └── popup.css
│   │   └── lib
│   │       └── api.ts
│   ├── package.json
│   └── tsconfig.json
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── core
│   │   │   └── config.py
│   │   ├── api
│   │   │   └── v1
│   │   │       ├── routes
│   │   │       │   ├── offers.py
│   │   │       │   └── verify.py
│   │   │       └── dependencies.py
│   │   ├── models
│   │   │   └── offer.py
│   │   ├── schemas
│   │   │   └── offer.py
│   │   ├── services
│   │   │   ├── scrapers.py
│   │   │   └── verifier.py
│   │   └── db
│   │       ├── base.py
│   │       └── session.py
│   ├── tests
│   │   ├── unit
│   │   │   └── test_verifier.py
│   │   └── integration
│   │       └── test_api.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── alembic
│   │   └── env.py
│   └── .env.example
├── infra
│   ├── docker-compose.yml
│   ├── k8s
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── helm
│       └── Chart.yaml
├── .github
│   └── workflows
│       └── ci.yml
├── scripts
│   ├── run_local.sh
│   └── deploy.sh
├── LICENSE
└── README.md
```

## Features

- **Chrome Extension**: A user-friendly interface that allows users to check discounts directly from their browser.
- **FastAPI Backend**: A robust backend that handles requests, verifies discounts, and interacts with the database.
- **Data Scraping**: The backend includes services to scrape data from e-commerce sites for accurate price comparisons.
- **Testing**: Comprehensive unit and integration tests to ensure the reliability of the application.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd AsliDeal
   ```

2. **Chrome Extension**:
   - Navigate to the `chrome-extension` directory.
   - Install dependencies:
     ```bash
     npm install
     ```
   - Load the extension in Chrome by navigating to `chrome://extensions`, enabling "Developer mode", and clicking "Load unpacked". Select the `chrome-extension` directory.

3. **Backend**:
   - Navigate to the `backend` directory.
   - Create a virtual environment and activate it:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the FastAPI application:
     ```bash
     uvicorn app.main:app --reload
     ```

4. **Database Setup**:
   - Configure your database settings in the `.env.example` file and rename it to `.env`.
   - Run migrations using Alembic.

## API Examples

- **Verify Discount**:
  - Endpoint: `POST /api/v1/verify`
  - Request Body: `{ "product_url": "https://example.com/product" }`
  - Response: `{ "is_valid": true, "discount": "20%" }`

## Testing

- To run unit tests:
  ```bash
  pytest backend/tests/unit
  ```
- To run integration tests:
  ```bash
  pytest backend/tests/integration
  ```

## Deployment

- Use the provided `docker-compose.yml` for local deployment.
- For production, follow the scripts in the `scripts` directory.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.