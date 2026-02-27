from django.contrib import admin
from .models import FAQEntry


@admin.register(FAQEntry)
class FAQEntryAdmin(admin.ModelAdmin):
    list_display = ['question', 'order']
    search_fields = ['question', 'answer']
    ordering = ['order']
