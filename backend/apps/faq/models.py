import uuid
from django.db import models


class FAQEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=500)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = 'faq'
        ordering = ['order']

    def __str__(self):
        return self.question
