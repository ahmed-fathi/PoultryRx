from django.contrib import admin
from .models import UserProfile, Article


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'public_articles_count']
    search_fields = ['username', 'first_name', 'last_name']
    ordering = ['username']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'author', 'status', 'is_featured',
        'publish_date', 'estimated_read_time', 'created_at',
    ]
    list_filter = ['status', 'is_featured', 'author']
    search_fields = ['title', 'slug', 'excerpt', 'author__username']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_date'
    ordering = ['-publish_date']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'author', 'status', 'is_featured')}),
        ('Content', {'fields': ('excerpt', 'content', 'cover_image', 'media')}),
        ('Metadata', {'fields': ('publish_date', 'estimated_read_time', 'created_at', 'updated_at')}),
    )
