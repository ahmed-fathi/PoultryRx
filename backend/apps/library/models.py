import uuid

from django.db import models


class LibraryResource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    mock_download_url = models.CharField(max_length=255)

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title


class FAQEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=500)
    answer = models.TextField()

    class Meta:
        ordering = ["question"]
        verbose_name_plural = "FAQ entries"

    def __str__(self) -> str:
        return self.question
