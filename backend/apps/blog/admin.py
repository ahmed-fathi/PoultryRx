from django.contrib import admin
from .models import Article, ArticleMedia


class ArticleMediaInline(admin.TabularInline):
    model = ArticleMedia
    extra = 0
    fields = ['url', 'mime_type', 'size_bytes']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'is_featured', 'publish_date', 'created_at']
    list_filter = ['status', 'is_featured']
    search_fields = ['title', 'slug', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ArticleMediaInline]
    date_hierarchy = 'publish_date'
    ordering = ['-publish_date']


@admin.register(ArticleMedia)
class ArticleMediaAdmin(admin.ModelAdmin):
    list_display = ['article', 'mime_type', 'size_bytes']
    search_fields = ['article__title']
