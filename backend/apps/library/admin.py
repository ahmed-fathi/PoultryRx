from django.contrib import admin
from .models import LibraryResource, FAQEntry


@admin.register(LibraryResource)
class LibraryResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'file_size_bytes', 'mock_download_url']
    list_filter = ['type']
    search_fields = ['title']
    ordering = ['title']


@admin.register(FAQEntry)
class FAQEntryAdmin(admin.ModelAdmin):
    list_display = ['question', 'order']
    search_fields = ['question', 'answer']
    ordering = ['order']
