import uuid
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('under_review', 'Under Review'),
        ('published', 'Published'),
        ('rejected', 'Rejected'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True, allow_unicode=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='articles'
    )
    publish_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    cover_image = models.URLField(blank=True)
    estimated_read_time = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'blog'
        ordering = ['-publish_date']

    def __str__(self):
        return self.title


class ArticleMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='media')
    url = models.URLField()
    mime_type = models.CharField(max_length=100)
    size_bytes = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = 'blog'

    def __str__(self):
        return f"{self.article.title} — {self.mime_type}"
