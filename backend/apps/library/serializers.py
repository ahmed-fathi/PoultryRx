from rest_framework import serializers
from .models import LibraryResource


class LibraryResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryResource
        fields = ['id', 'title', 'type', 'mock_download_url']
