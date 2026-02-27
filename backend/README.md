# PoultryRx Backend

Django REST API backend for the PoultryRx knowledge platform.

## Quick Start (SQLite — development)

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Admin dashboard: http://localhost:8000/admin/  
REST API base: http://localhost:8000/api/v1/

## PostgreSQL Setup

Copy `.env.example` to `.env` and fill in database credentials, then run migrations.

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/v1/landing/featured` | 5 latest featured articles |
| GET | `/api/v1/blog/` | Paginated blog listing |
| GET | `/api/v1/articles/{slug}/` | Article detail |
| GET | `/api/v1/profiles/{username}/public` | Public profile |
| GET | `/api/v1/tools/` | AI tools list |
| GET | `/api/v1/library/` | Library resources |
| GET | `/api/v1/faq/` | FAQ entries |

## Project Structure

```
backend/
├── manage.py
├── requirements.txt
├── .env.example
├── config/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── apps/
    ├── api_urls.py      # Aggregated API routes
    ├── blog/            # Articles & media
    ├── profiles/        # Public user profiles
    ├── tools/           # AI tools
    ├── library/         # Library resources
    └── faq/             # FAQ entries
```
