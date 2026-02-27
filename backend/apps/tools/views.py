from rest_framework import generics
from .models import Tool
from .serializers import ToolSerializer


class ToolListView(generics.ListAPIView):
    """GET /api/v1/tools/ — list all tools."""

    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    pagination_class = None  # return all tools without pagination

    def list(self, request, *args, **kwargs):
        from rest_framework.response import Response
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        return Response({'results': serializer.data})
