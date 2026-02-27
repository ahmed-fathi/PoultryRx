import uuid
from django.db import models


class Tool(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True, allow_unicode=True)
    description = models.TextField(blank=True)
    entry_point = models.CharField(max_length=500, help_text='Frontend route or external URL')
    example_input = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Tool'
        verbose_name_plural = 'Tools'

    def __str__(self):
        return self.name
