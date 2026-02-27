from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'total_read_count', 'public_articles_count']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    readonly_fields = ['public_articles_count']

    def username(self, obj):
        return obj.user.username

    def full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}".strip()

    username.short_description = 'Username'
    full_name.short_description = 'Full Name'
