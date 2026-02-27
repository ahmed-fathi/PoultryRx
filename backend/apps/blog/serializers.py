from rest_framework import serializers
from .models import UserProfile, Article


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name']


class ArticleListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'slug', 'excerpt',
            'author', 'publish_date', 'cover_image',
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt',
            'media', 'estimated_read_time',
            'author', 'publish_date', 'cover_image', 'status',
        ]


class PublicArticleRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug']


class UserProfileSerializer(serializers.ModelSerializer):
    public_articles_count = serializers.IntegerField(read_only=True)
    total_read_count = serializers.IntegerField(read_only=True)
    public_articles = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            'username', 'first_name', 'last_name',
            'public_articles_count', 'total_read_count',
            'public_articles',
        ]

    def get_public_articles(self, obj):
        qs = obj.articles.filter(status='published').order_by('-publish_date')
        return PublicArticleRefSerializer(qs, many=True).data
