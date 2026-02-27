# PoultryRx Backend (Django + DRF)

This backend serves the REST API described in `specs/002-add-landing-blog/contracts/rest-endpoints.md`.

## Prereqs

- Python (use the repo `.venv` or create one)
- PostgreSQL (recommended via Docker Compose)

## Install

From repo root:

```bash
# create/activate your venv (example)
python -m venv .venv
# Windows PowerShell:
# .\.venv\Scripts\Activate.ps1

pip install -r backend/requirements.txt
```

## Run with PostgreSQL

1) Start Postgres:

```bash
docker compose up -d db
```

2) Run migrations + seed:

```bash
cd backend
python manage.py migrate
python manage.py seed_mock_data
python manage.py runserver 8000
```

## Run with SQLite (quick local smoke test)

```bash
cd backend
set DATABASE_URL=sqlite:///db.sqlite3  # PowerShell: $env:DATABASE_URL='sqlite:///db.sqlite3'
python manage.py migrate
python manage.py seed_mock_data
python manage.py runserver 8000
```

## Frontend connection

- Vite proxy is configured so `/api/*` in the frontend dev server proxies to `http://localhost:8000`.
- To use the real backend instead of fixtures:

```bash
cd frontend
VITE_API_MODE=real npm run dev
```

Default is `VITE_API_MODE=mock`.
