from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination

from .models import Article, UserProfile
from .serializers import (
    ArticleListSerializer,
    ArticleDetailSerializer,
    UserProfileSerializer,
)


class BlogPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'results': data,
            'page': self.page.number,
            'page_size': self.get_page_size(self.request),
            'total': self.page.paginator.count,
        })


class FeaturedArticlesView(APIView):
    """GET /api/v1/landing/featured — up to 5 featured published articles."""

    def get(self, request):
        qs = (
            Article.objects
            .filter(status='published', is_featured=True)
            .select_related('author')
            .order_by('-publish_date')[:5]
        )
        serializer = ArticleListSerializer(qs, many=True)
        return Response({'articles': serializer.data})


class BlogListView(generics.ListAPIView):
    """GET /api/v1/blog/ — paginated published articles."""

    serializer_class = ArticleListSerializer
    pagination_class = BlogPagination

    def get_queryset(self):
        return (
            Article.objects
            .filter(status='published')
            .select_related('author')
            .order_by('-publish_date')
        )


class ArticleDetailView(generics.RetrieveAPIView):
    """GET /api/v1/articles/{slug}/ — article detail."""

    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Article.objects.filter(status='published').select_related('author')


class PublicProfileView(APIView):
    """GET /api/v1/profiles/{username}/public — public user profile."""

    def get(self, request, username):
        try:
            profile = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return Response(
                {'detail': 'Profile not found.'},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
