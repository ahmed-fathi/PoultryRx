from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class PublicAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class PublicProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    public_articles_count = serializers.IntegerField(read_only=True)
    public_articles = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            'username', 'first_name', 'last_name',
            'public_articles_count', 'total_read_count', 'public_articles',
        ]

    def get_public_articles(self, obj):
        from apps.blog.serializers import ArticleSummarySerializer
        qs = obj.user.articles.filter(status='published').values('id', 'title', 'slug')
        return list(qs)
