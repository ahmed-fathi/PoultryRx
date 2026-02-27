import uuid
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    total_read_count = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = 'profiles'

    def __str__(self):
        return self.user.username

    @property
    def public_articles_count(self):
        return self.user.articles.filter(status='published').count()
