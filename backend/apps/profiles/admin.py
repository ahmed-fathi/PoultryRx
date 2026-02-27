from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'public_articles_count', 'total_read_count', 'created_at')
    search_fields = ('username', 'first_name', 'last_name')