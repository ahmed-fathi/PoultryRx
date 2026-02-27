from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.v1.serializers import (
    ArticleDetailSerializer,
    ArticleListSerializer,
    FAQEntrySerializer,
    LibraryResourceSerializer,
    ProfilePublicSerializer,
    ToolSerializer,
    estimate_read_time_minutes,
)
from apps.blog.models import Article
from apps.library.models import FAQEntry, LibraryResource
from apps.profiles.models import UserProfile
from apps.tools.models import Tool


class LandingFeaturedView(APIView):
    """GET /api/v1/landing/featured — up to 5 featured published articles."""

    permission_classes = [AllowAny]

    def get(self, request):
        qs = (
            Article.objects.filter(status="published", is_featured=True)
            .select_related("author")
            .order_by("-publish_date")[:5]
        )
        serializer = ArticleListSerializer(qs, many=True)
        return Response({"articles": serializer.data})


class BlogListView(APIView):
    """GET /api/v1/blog/?page=1&page_size=20 — paginated blog listing."""

    permission_classes = [AllowAny]

    def get(self, request):
        try:
            page = max(1, int(request.query_params.get("page", "1")))
        except (ValueError, TypeError):
            page = 1

        try:
            page_size = min(max(1, int(request.query_params.get("page_size", "20"))), 100)
        except (ValueError, TypeError):
            page_size = 20

        qs = (
            Article.objects.filter(status="published")
            .select_related("author")
            .order_by("-publish_date")
        )
        total = qs.count()
        start = (page - 1) * page_size
        results = qs[start : start + page_size]

        serializer = ArticleListSerializer(results, many=True)
        return Response(
            {
                "results": serializer.data,
                "page": page,
                "page_size": page_size,
                "total": total,
            }
        )


class ArticleDetailView(generics.RetrieveAPIView):
    """GET /api/v1/articles/{slug}/ — article detail."""

    permission_classes = [AllowAny]
    serializer_class = ArticleDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return (
            Article.objects.filter(status="published")
            .select_related("author")
            .prefetch_related("media")
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Auto-compute read time if missing
        if not instance.estimated_read_time or instance.estimated_read_time <= 1:
            instance.estimated_read_time = estimate_read_time_minutes(instance.content)
            instance.save(update_fields=["estimated_read_time"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ProfilePublicView(generics.RetrieveAPIView):
    """GET /api/v1/profiles/{username}/public — public profile."""

    permission_classes = [AllowAny]
    serializer_class = ProfilePublicSerializer
    lookup_field = "username"
    queryset = UserProfile.objects.all()


class ToolsListView(generics.ListAPIView):
    """GET /api/v1/tools/ — all tools."""

    permission_classes = [AllowAny]
    serializer_class = ToolSerializer
    queryset = Tool.objects.all().order_by("name")

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({"results": response.data})


class LibraryListView(generics.ListAPIView):
    """GET /api/v1/library/ — library resources."""

    permission_classes = [AllowAny]
    serializer_class = LibraryResourceSerializer
    queryset = LibraryResource.objects.all().order_by("title")

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({"results": response.data})


class FAQListView(generics.ListAPIView):
    """GET /api/v1/faq/ — FAQ entries."""

    permission_classes = [AllowAny]
    serializer_class = FAQEntrySerializer
    queryset = FAQEntry.objects.all()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({"results": response.data})
