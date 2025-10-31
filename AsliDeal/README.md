# AsliDeal

AsliDeal is a full-stack application designed to verify discount offers on Pakistani e-commerce sites. The project consists of a Chrome extension that interacts with a FastAPI backend to provide users with reliable information about discounts and offers.

## Project Structure

```
AsliDeal
# AsliDeal — Real vs Fake Discount Verifier

AsliDeal helps users verify whether discount offers on Pakistani e-commerce sites are genuine or fake. It consists of a Chrome extension (frontend) and a FastAPI backend that scrapes/records prices, runs OCR on screenshots, and assesses discounts based on historical price data.

This repository contains the full-stack implementation and CI/CD for deploying the backend to AWS EC2 via Docker/ECR.

## Key components

- `AsliDeal/backend` — FastAPI application, SQLAlchemy models, tests, and Dockerfile
- `AsliDeal/chrome-extension` — Manifest V3 extension, React/Vite popup and background scripts
- `AsliDeal/docker-compose.yml` — Production compose for backend + PostgreSQL
- `AsliDeal/deploy.sh` — EC2 deploy script used by GitHub Actions
- `.github/workflows/ci-cd.yml` — CI pipeline: tests, build/push to ECR, remote deploy to EC2

## Table of contents

- Features
- Architecture
- Quick start (local)
- Production deploy (GitHub Actions → ECR → EC2)
- API examples
- Environment & configuration
- Testing
- Developer notes
- Contributing
- License

## Features

- Verify whether a claimed discount is valid using historical price checks
- Screenshot upload + OCR (pytesseract / easyocr) support (backend endpoint)
- Chrome extension popup with historical price and verdict (Asli Deal / Nakli Deal)
- Background scheduler (periodic checks) and scraping modules
- Dockerized backend + Postgres for local development and production

## Architecture (high-level)

- **Chrome Extension (MV3)**
  - Popup UI shows product info, historical price chart, verdict
  - Background script captures product page and sends screenshot to backend
  - Content script highlights fake discounts on-page

- **Backend (FastAPI)**
  - `/api/v1/offers` — CRUD for tracked products
  - `/api/v1/price-history` — Fetch price history
  - `/api/v1/verify` — Analyze a product and return verdict
  - `/api/v1/upload` — Accept screenshots and run OCR
  - Services: scrapers, verifier, OCR integration
  - DB: PostgreSQL via SQLAlchemy; Alembic for migrations

## Quick start (local development)

### Prerequisites

- Python 3.11+ (for running tests locally)
- Docker & Docker Compose (for running stack locally)
- Node & npm (for building the extension)

### 1) Clone the repository

```bash
git clone https://github.com/<your-org>/DealCheckr.git
cd DealCheckr/AsliDeal
```

### 2) Run backend (development)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3) Run full stack locally with Docker Compose

```bash
# from repo root (AsliDeal)
docker compose up --build
```

This will start the backend (reads `IMAGE_FULL` from env) and a Postgres database. Use `.env` (or copy `.env.example`) to set DB credentials and image values.

## Production deploy (CI/CD summary)

- Push to `main` or open a PR to `main` → GitHub Actions triggers.
- Workflow steps (see `.github/workflows/ci-cd.yml`):
  1. Run pytest (unit & integration)
  2. Build and push Docker image to AWS ECR (tag: short SHA)
  3. Upload `deploy.sh` + `docker-compose.yml` to EC2 and run `deploy.sh <IMAGE_FULL>` via SSH

### EC2 deploy details

- The `deploy.sh` placed on EC2 will:
  - Save/record the previous image tag
  - Update `.env` with `IMAGE_FULL` for the `docker-compose.yml`
  - Pull the new image and run `docker compose up -d --no-build`
  - If deployment fails, it attempts to restore the previous image and restart it (basic rollback)

## GitHub Secrets required

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `ECR_REPOSITORY`
- `EC2_HOST`
- `EC2_USER`
- `EC2_SSH_KEY` (private key contents)

## API examples

### Verify discount

Request

```http
POST /api/v1/verify/
Content-Type: application/json

{
  "product_id": "12345",
  "current_price": 1000
}
```

Response (example)

```json
{
  "valid": true,
  "message": "Discount is valid."
}
```

## Environment variables

- See `AsliDeal/.env.example` for the minimal set used by `docker-compose.yml`.
- Common env keys:
  - `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`
  - `IMAGE_FULL` — fully-qualified image to run in production (ECR URI)

## Testing

- Run backend tests locally:

```bash
cd AsliDeal/backend
PYTHONPATH=. pytest -q
```

- CI automatically runs the same tests on each push/PR.

## Developer notes & next steps

- The current repository includes a test-focused verifier stub used by integration tests; production should replace in-memory stubs with DB-backed lookups and full scraping/OCR.
- Recommended additions:
  - Alembic migrations for DB schema (one-time migration files)
  - Celery + Redis for heavy background scraping tasks
  - Blue/green deployment or healthcheck-based swapping for zero-downtime deploys

## Contributing

- Please open issues for bugs or new features.
- Follow the coding style: Black + isort for Python; Prettier + ESLint for TypeScript.

## License

- MIT — see the LICENSE file.

## Contact

- For questions, open an issue or contact the repository owner.
