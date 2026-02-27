from django.contrib import admin
from .models import Article, ArticleMedia

class ArticleMediaInline(admin.TabularInline):
    model = ArticleMedia
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'publish_date', 'is_featured')
    list_filter = ('status', 'is_featured', 'publish_date')
    search_fields = ('title', 'slug', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ArticleMediaInline]

@admin.register(ArticleMedia)
class ArticleMediaAdmin(admin.ModelAdmin):
    list_display = ('article', 'url', 'mime_type', 'size_bytes')
    search_fields = ('url',)