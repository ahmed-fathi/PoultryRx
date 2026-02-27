from rest_framework import serializers
from .models import LibraryResource, FAQEntry


class LibraryResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryResource
        fields = ['id', 'title', 'type', 'mock_download_url', 'file_size_bytes']


class FAQEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQEntry
        fields = ['id', 'question', 'answer']
