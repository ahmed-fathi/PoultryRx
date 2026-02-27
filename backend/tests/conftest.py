"""Pytest / Django configuration for backend tests."""

import os

import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poultryrx.settings")

# Force SQLite for tests regardless of DATABASE_URL
os.environ["DATABASE_URL"] = "sqlite:///test.sqlite3"

django.setup()
