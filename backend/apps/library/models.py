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
    mock_download_url = models.URLField()
    file_size_bytes = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = 'library'

    def __str__(self):
        return self.title
