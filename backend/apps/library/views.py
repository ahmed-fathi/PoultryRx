from rest_framework import generics
from rest_framework.response import Response
from .models import LibraryResource, FAQEntry
from .serializers import LibraryResourceSerializer, FAQEntrySerializer


class LibraryListView(generics.ListAPIView):
    """GET /api/v1/library/ — list all library resources."""

    queryset = LibraryResource.objects.all()
    serializer_class = LibraryResourceSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        return Response({'results': serializer.data})


class FAQListView(generics.ListAPIView):
    """GET /api/v1/faq/ — list all FAQ entries."""

    queryset = FAQEntry.objects.all()
    serializer_class = FAQEntrySerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        return Response({'results': serializer.data})
