from rest_framework import serializers
from .models import Article, ArticleMedia


class ArticleMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleMedia
        fields = ['url', 'mime_type']


class ArticleSummarySerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'excerpt', 'cover_image', 'publish_date', 'author']

    def get_author(self, obj):
        if obj.author:
            return {
                'username': obj.author.username,
                'first_name': obj.author.first_name,
                'last_name': obj.author.last_name,
            }
        return None


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    media = ArticleMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt', 'cover_image',
            'media', 'estimated_read_time', 'author', 'publish_date',
        ]

    def get_author(self, obj):
        if obj.author:
            return {
                'username': obj.author.username,
                'first_name': obj.author.first_name,
                'last_name': obj.author.last_name,
            }
        return None
