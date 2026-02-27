import math
import re

from rest_framework import serializers

from apps.blog.models import Article, ArticleMedia
from apps.library.models import FAQEntry, LibraryResource
from apps.profiles.models import UserProfile
from apps.tools.models import Tool


_TAG_RE = re.compile(r"<[^>]+>")


def estimate_read_time_minutes(html: str) -> int:
    """Estimate reading time from HTML content (approx 200 wpm)."""
    text = _TAG_RE.sub(" ", html or "")
    words = [w for w in text.split() if w.strip()]
    return max(1, math.ceil(len(words) / 200))


# ----- Profile -----


class AuthorPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["username", "first_name", "last_name"]


class ProfilePublicSerializer(serializers.ModelSerializer):
    public_articles = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            "username",
            "first_name",
            "last_name",
            "public_articles_count",
            "total_read_count",
            "public_articles",
        ]

    def get_public_articles(self, obj: UserProfile):
        qs = (
            obj.articles.filter(status="published")
            .only("id", "title", "slug", "publish_date")
            .order_by("-publish_date")
        )
        return [
            {"id": str(a.id), "title": a.title, "slug": a.slug}
            for a in qs
        ]


# ----- Blog / Article -----


class ArticleListSerializer(serializers.ModelSerializer):
    author = AuthorPublicSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "slug",
            "excerpt",
            "cover_image",
            "publish_date",
            "author",
        ]


class ArticleMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleMedia
        fields = ["url", "mime_type"]


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = AuthorPublicSerializer(read_only=True)
    media = ArticleMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "media",
            "estimated_read_time",
            "author",
            "publish_date",
        ]


# ----- Tools -----


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ["id", "name", "slug", "description", "entry_point"]


# ----- Library / FAQ -----


class LibraryResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryResource
        fields = ["id", "title", "type", "mock_download_url"]


class FAQEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQEntry
        fields = ["id", "question", "answer"]
