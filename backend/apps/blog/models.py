import uuid
from django.db import models


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['username']
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.username

    @property
    def public_articles_count(self):
        return self.articles.filter(status='published').count()

    @property
    def total_read_count(self):
        """Sum of estimated_read_time for all published articles (proxy metric)."""
        from django.db.models import Sum
        result = self.articles.filter(status='published').aggregate(
            total=Sum('estimated_read_time')
        )
        return result['total'] or 0


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
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles',
    )
    publish_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    cover_image = models.URLField(max_length=500, blank=True)
    # media stored as a JSON array: [{"url": "...", "mime_type": "..."}]
    media = models.JSONField(default=list, blank=True)
    estimated_read_time = models.PositiveIntegerField(default=1, help_text='Minutes')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        from django.utils import timezone
        now = timezone.now()
        if self.created_at is None:
            self.created_at = now
        self.updated_at = now
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-publish_date', '-created_at']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
