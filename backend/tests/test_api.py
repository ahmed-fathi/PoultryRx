"""API endpoint tests for the PoultryRx backend.

Tests every public endpoint against the REST contract shapes defined in
specs/002-add-landing-blog/contracts/rest-endpoints.md
"""

import uuid

from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient

from apps.blog.models import Article, ArticleMedia
from apps.library.models import FAQEntry, LibraryResource
from apps.profiles.models import UserProfile
from apps.tools.models import Tool


class _SeedMixin:
    """Shared seed helper used by multiple test classes."""

    @classmethod
    def _seed(cls):
        cls.author = UserProfile.objects.create(
            username="test_author",
            first_name="Test",
            last_name="Author",
            public_articles_count=3,
            total_read_count=100,
        )
        now = timezone.now()
        cls.articles = []
        for i in range(5):
            a = Article.objects.create(
                title=f"Article {i}",
                slug=f"article-{i}",
                excerpt=f"Excerpt {i}",
                content=f"<p>{'word ' * 400}</p>",
                author=cls.author,
                publish_date=now - timezone.timedelta(days=i),
                cover_image=f"https://example.com/img{i}.jpg",
                status="published",
                is_featured=i < 3,
            )
            cls.articles.append(a)
        # One draft article — should NOT appear in public endpoints
        cls.draft = Article.objects.create(
            title="Draft article",
            slug="draft-article",
            excerpt="Draft excerpt",
            content="<p>draft</p>",
            author=cls.author,
            status="draft",
        )
        ArticleMedia.objects.create(
            article=cls.articles[0],
            url="https://example.com/vid.mp4",
            mime_type="video/mp4",
        )
        cls.tool = Tool.objects.create(
            name="Feed Calculator",
            slug="feed-calculator",
            description="Calculates feed.",
            entry_point="/tools/feed-calculator",
        )
        cls.resource = LibraryResource.objects.create(
            title="Guide PDF",
            type="pdf",
            mock_download_url="/downloads/guide.pdf",
        )
        cls.faq = FAQEntry.objects.create(
            question="What is PoultryRx?",
            answer="A platform for poultry science.",
        )


class LandingFeaturedTests(_SeedMixin, TestCase):
    @classmethod
    def setUpTestData(cls):
        cls._seed()

    def setUp(self):
        self.client = APIClient()

    def test_status_200(self):
        resp = self.client.get("/api/v1/landing/featured")
        self.assertEqual(resp.status_code, 200)

    def test_response_shape(self):
        resp = self.client.get("/api/v1/landing/featured")
        data = resp.json()
        self.assertIn("articles", data)
        self.assertIsInstance(data["articles"], list)

    def test_returns_only_featured(self):
        resp = self.client.get("/api/v1/landing/featured")
        data = resp.json()
        self.assertEqual(len(data["articles"]), 3)  # only 3 are featured

    def test_article_keys(self):
        resp = self.client.get("/api/v1/landing/featured")
        art = resp.json()["articles"][0]
        for key in ("id", "title", "slug", "excerpt", "cover_image", "publish_date", "author"):
            self.assertIn(key, art, f"Missing key: {key}")

    def test_author_sub_shape(self):
        resp = self.client.get("/api/v1/landing/featured")
        author = resp.json()["articles"][0]["author"]
        for key in ("username", "first_name", "last_name"):
            self.assertIn(key, author)

    def test_excludes_drafts(self):
        resp = self.client.get("/api/v1/landing/featured")
        slugs = [a["slug"] for a in resp.json()["articles"]]
        self.assertNotIn("draft-article", slugs)


class BlogListTests(_SeedMixin, TestCase):
    @classmethod
    def setUpTestData(cls):
        cls._seed()

    def setUp(self):
        self.client = APIClient()

    def test_status_200(self):
        resp = self.client.get("/api/v1/blog/")
        self.assertEqual(resp.status_code, 200)

    def test_response_shape(self):
        data = self.client.get("/api/v1/blog/").json()
        for key in ("results", "page", "page_size", "total"):
            self.assertIn(key, data)

    def test_total_excludes_drafts(self):
        data = self.client.get("/api/v1/blog/").json()
        self.assertEqual(data["total"], 5)  # 5 published, 1 draft

    def test_pagination(self):
        data = self.client.get("/api/v1/blog/?page=1&page_size=2").json()
        self.assertEqual(len(data["results"]), 2)
        self.assertEqual(data["page"], 1)
        self.assertEqual(data["page_size"], 2)
        self.assertEqual(data["total"], 5)

    def test_ordered_newest_first(self):
        data = self.client.get("/api/v1/blog/").json()
        dates = [r["publish_date"] for r in data["results"]]
        self.assertEqual(dates, sorted(dates, reverse=True))


class ArticleDetailTests(_SeedMixin, TestCase):
    @classmethod
    def setUpTestData(cls):
        cls._seed()

    def setUp(self):
        self.client = APIClient()

    def test_status_200(self):
        resp = self.client.get(f"/api/v1/articles/{self.articles[0].slug}/")
        self.assertEqual(resp.status_code, 200)

    def test_response_shape(self):
        data = self.client.get(f"/api/v1/articles/{self.articles[0].slug}/").json()
        for key in ("id", "title", "slug", "content", "media", "estimated_read_time", "author", "publish_date"):
            self.assertIn(key, data, f"Missing key: {key}")

    def test_media_included(self):
        data = self.client.get(f"/api/v1/articles/{self.articles[0].slug}/").json()
        self.assertEqual(len(data["media"]), 1)
        self.assertIn("url", data["media"][0])
        self.assertIn("mime_type", data["media"][0])

    def test_draft_returns_404(self):
        resp = self.client.get("/api/v1/articles/draft-article/")
        self.assertEqual(resp.status_code, 404)

    def test_nonexistent_returns_404(self):
        resp = self.client.get("/api/v1/articles/no-such-slug/")
        self.assertEqual(resp.status_code, 404)

    def test_read_time_auto_computed(self):
        data = self.client.get(f"/api/v1/articles/{self.articles[0].slug}/").json()
        self.assertGreater(data["estimated_read_time"], 0)


class ProfilePublicTests(_SeedMixin, TestCase):
    @classmethod
    def setUpTestData(cls):
        cls._seed()

    def setUp(self):
        self.client = APIClient()

    def test_status_200(self):
        resp = self.client.get(f"/api/v1/profiles/{self.author.username}/public")
        self.assertEqual(resp.status_code, 200)

    def test_response_shape(self):
        data = self.client.get(f"/api/v1/profiles/{self.author.username}/public").json()
        for key in ("username", "first_name", "last_name", "public_articles_count", "total_read_count", "public_articles"):
            self.assertIn(key, data, f"Missing key: {key}")

    def test_public_articles_list(self):
        data = self.client.get(f"/api/v1/profiles/{self.author.username}/public").json()
        self.assertEqual(len(data["public_articles"]), 5)  # 5 published
        art = data["public_articles"][0]
        for key in ("id", "title", "slug"):
            self.assertIn(key, art)

    def test_nonexistent_returns_404(self):
        resp = self.client.get("/api/v1/profiles/nobody/public")
        self.assertEqual(resp.status_code, 404)


class ToolsListTests(_SeedMixin, TestCase):
    @classmethod
    def setUpTestData(cls):
        cls._seed()

    def setUp(self):
        self.client = APIClient()

    def test_status_200(self):
        resp = self.client.get("/api/v1/tools/")
        self.assertEqual(resp.status_code, 200)

    def test_response_shape(self):
        data = self.client.get("/api/v1/tools/").json()
        self.assertIn("results", data)
        self.assertEqual(len(data["results"]), 1)

    def test_tool_keys(self):
        tool = self.client.get("/api/v1/tools/").json()["results"][0]
        for key in ("id", "name", "slug", "description", "entry_point"):
            self.assertIn(key, tool, f"Missing key: {key}")


class LibraryListTests(_SeedMixin, TestCase):
    @classmethod
    def setUpTestData(cls):
        cls._seed()

    def setUp(self):
        self.client = APIClient()

    def test_status_200(self):
        resp = self.client.get("/api/v1/library/")
        self.assertEqual(resp.status_code, 200)

    def test_response_shape(self):
        data = self.client.get("/api/v1/library/").json()
        self.assertIn("results", data)
        self.assertEqual(len(data["results"]), 1)

    def test_resource_keys(self):
        res = self.client.get("/api/v1/library/").json()["results"][0]
        for key in ("id", "title", "type", "mock_download_url"):
            self.assertIn(key, res, f"Missing key: {key}")


class FAQListTests(_SeedMixin, TestCase):
    @classmethod
    def setUpTestData(cls):
        cls._seed()

    def setUp(self):
        self.client = APIClient()

    def test_status_200(self):
        resp = self.client.get("/api/v1/faq/")
        self.assertEqual(resp.status_code, 200)

    def test_response_shape(self):
        data = self.client.get("/api/v1/faq/").json()
        self.assertIn("results", data)
        self.assertEqual(len(data["results"]), 1)

    def test_faq_keys(self):
        entry = self.client.get("/api/v1/faq/").json()["results"][0]
        for key in ("id", "question", "answer"):
            self.assertIn(key, entry, f"Missing key: {key}")


class ModelTests(TestCase):
    """Unit tests for model validation and constraints."""

    def test_article_uuid_pk(self):
        profile = UserProfile.objects.create(username="uuid_test")
        article = Article.objects.create(
            title="T", slug="uuid-test", author=profile, status="draft"
        )
        self.assertIsInstance(article.id, uuid.UUID)

    def test_article_slug_unique(self):
        profile = UserProfile.objects.create(username="slug_dup")
        Article.objects.create(title="A1", slug="dup-slug", author=profile)
        with self.assertRaises(Exception):
            Article.objects.create(title="A2", slug="dup-slug", author=profile)

    def test_profile_username_unique(self):
        UserProfile.objects.create(username="one")
        with self.assertRaises(Exception):
            UserProfile.objects.create(username="one")

    def test_article_has_timestamps(self):
        profile = UserProfile.objects.create(username="ts_test")
        a = Article.objects.create(title="TS", slug="ts-test", author=profile)
        self.assertIsNotNone(a.created_at)
        self.assertIsNotNone(a.updated_at)

    def test_profile_has_timestamps(self):
        p = UserProfile.objects.create(username="pts_test")
        self.assertIsNotNone(p.created_at)
        self.assertIsNotNone(p.updated_at)

    def test_article_protect_author_delete(self):
        """Deleting a profile that has articles should raise ProtectedError."""
        profile = UserProfile.objects.create(username="protect_test")
        Article.objects.create(title="P", slug="protect-test", author=profile)
        from django.db.models import ProtectedError
        with self.assertRaises(ProtectedError):
            profile.delete()
