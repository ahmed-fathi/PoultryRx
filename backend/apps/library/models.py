import uuid
from django.db import models


class LibraryResource(models.Model):
    TYPE_CHOICES = [
        ('pdf', 'PDF'),
        ('image', 'Image'),
        ('excel', 'Excel'),
        ('template', 'Template'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    mock_download_url = models.URLField(max_length=500, blank=True)
    file_size_bytes = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Library Resource'
        verbose_name_plural = 'Library Resources'

    def __str__(self):
        return self.title


class FAQEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=500)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0, help_text='Display order (lower = first)')

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'FAQ Entry'
        verbose_name_plural = 'FAQ Entries'

    def __str__(self):
        return self.question[:80]
