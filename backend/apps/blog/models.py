import uuid

from django.db import models


class ArticleStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    UNDER_REVIEW = "under_review", "Under review"
    PUBLISHED = "published", "Published"
    REJECTED = "rejected", "Rejected"


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField(blank=True)  # sanitized HTML

    author = models.ForeignKey(
        "profiles.UserProfile",
        on_delete=models.PROTECT,
        related_name="articles",
    )
    publish_date = models.DateTimeField(null=True, blank=True)
    cover_image = models.TextField(blank=True)  # URL, stored as text to allow long URLs
    status = models.CharField(
        max_length=20,
        choices=ArticleStatus.choices,
        default=ArticleStatus.DRAFT,
        db_index=True,
    )
    is_featured = models.BooleanField(default=False, db_index=True)
    estimated_read_time = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-publish_date"]
        indexes = [
            models.Index(fields=["-publish_date", "status"]),
            models.Index(fields=["author", "status"]),
        ]

    def __str__(self) -> str:
        return self.title


class ArticleMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="media")
    url = models.URLField()
    mime_type = models.CharField(max_length=100, blank=True)
    size_bytes = models.BigIntegerField(default=0)
