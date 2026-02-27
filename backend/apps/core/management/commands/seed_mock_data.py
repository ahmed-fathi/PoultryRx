import json
from pathlib import Path

import bleach
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime, parse_date

from apps.blog.models import Article, ArticleMedia
from apps.library.models import FAQEntry, LibraryResource
from apps.profiles.models import UserProfile
from apps.tools.models import Tool


ALLOWED_TAGS = [
    "p", "br", "strong", "em", "ul", "ol", "li", "a",
    "h1", "h2", "h3", "blockquote", "code", "pre",
]
ALLOWED_ATTRS = {"a": ["href", "title", "rel", "target"]}


def _parse_publish_date(value):
    """Accept both datetime and date strings from fixture data."""
    if not value:
        return None
    from datetime import datetime as dt_class, time
    from django.utils.timezone import make_aware, is_aware

    parsed_dt = parse_datetime(value)
    if parsed_dt:
        return parsed_dt if is_aware(parsed_dt) else make_aware(parsed_dt)

    parsed_d = parse_date(value)
    if parsed_d:
        naive = dt_class.combine(parsed_d, time.min)
        return make_aware(naive)

    return None


class Command(BaseCommand):
    help = "Seed PostgreSQL with mock data from frontend/src/services/mockData/*.json"

    def handle(self, *args, **options):
        # Locate the repo root by walking up from this file
        seed_file = Path(__file__).resolve()
        repo_root = None
        for parent in seed_file.parents:
            if (parent / "frontend" / "src" / "services" / "mockData").exists():
                repo_root = parent
                break

        if not repo_root:
            raise RuntimeError(
                "Unable to locate repo root (expected frontend/src/services/mockData)."
            )

        mock_dir = repo_root / "frontend" / "src" / "services" / "mockData"

        # ---------- Profiles ----------
        profiles_path = mock_dir / "profiles.json"
        if profiles_path.exists():
            profiles = json.loads(profiles_path.read_text(encoding="utf-8"))
            for p in profiles:
                UserProfile.objects.update_or_create(
                    username=p["username"],
                    defaults={
                        "first_name": p.get("first_name", ""),
                        "last_name": p.get("last_name", ""),
                        "public_articles_count": int(p.get("public_articles_count", 0) or 0),
                        "total_read_count": int(p.get("total_read_count", 0) or 0),
                    },
                )
            self.stdout.write(f"  Profiles: {len(profiles)}")

        # ---------- Tools ----------
        tools_path = mock_dir / "tools.json"
        if tools_path.exists():
            tools = json.loads(tools_path.read_text(encoding="utf-8"))
            for t in tools:
                Tool.objects.update_or_create(
                    slug=t["slug"],
                    defaults={
                        "name": t["name"],
                        "description": t.get("description", ""),
                        "entry_point": t.get("entry_point", ""),
                    },
                )
            self.stdout.write(f"  Tools: {len(tools)}")

        # ---------- Library ----------
        library_path = mock_dir / "library.json"
        if library_path.exists():
            items = json.loads(library_path.read_text(encoding="utf-8"))
            for it in items:
                LibraryResource.objects.update_or_create(
                    title=it["title"],
                    defaults={
                        "type": it.get("type", ""),
                        "mock_download_url": it.get("mock_download_url", "#"),
                    },
                )
            self.stdout.write(f"  Library resources: {len(items)}")

        # ---------- FAQ ----------
        faq_path = mock_dir / "faq.json"
        if faq_path.exists():
            items = json.loads(faq_path.read_text(encoding="utf-8"))
            for it in items:
                FAQEntry.objects.update_or_create(
                    question=it["question"],
                    defaults={"answer": it.get("answer", "")},
                )
            self.stdout.write(f"  FAQ entries: {len(items)}")

        # ---------- Articles ----------
        articles_path = mock_dir / "articles.json"
        if articles_path.exists():
            items = json.loads(articles_path.read_text(encoding="utf-8"))
            for a in items:
                author_username = (a.get("author") or {}).get("username") or "unknown"
                author, _ = UserProfile.objects.get_or_create(
                    username=author_username,
                    defaults={"first_name": "", "last_name": ""},
                )

                raw_html = a.get("content", "") or ""
                cleaned = bleach.clean(
                    raw_html,
                    tags=ALLOWED_TAGS,
                    attributes=ALLOWED_ATTRS,
                    strip=True,
                )

                article, _ = Article.objects.update_or_create(
                    slug=a["slug"],
                    defaults={
                        "title": a["title"],
                        "excerpt": a.get("excerpt", ""),
                        "content": cleaned,
                        "author": author,
                        "publish_date": _parse_publish_date(a.get("publish_date")),
                        "cover_image": a.get("cover_image", ""),
                        "status": a.get("status", "published"),
                        "is_featured": bool(a.get("is_featured", False)),
                    },
                )

                # Re-create media attachments
                ArticleMedia.objects.filter(article=article).delete()
                for m in a.get("media", []) or []:
                    ArticleMedia.objects.create(
                        article=article,
                        url=m.get("url", ""),
                        mime_type=m.get("mime_type", ""),
                        size_bytes=m.get("size_bytes", 0) or 0,
                    )

            self.stdout.write(f"  Articles: {len(items)}")

        self.stdout.write(self.style.SUCCESS("Seed complete."))
