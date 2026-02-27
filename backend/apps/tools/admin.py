from django.contrib import admin
from .models import Tool

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'entry_point')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}