from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LibraryResource
from .serializers import LibraryResourceSerializer


@api_view(['GET'])
def library_list(request):
    resources = LibraryResource.objects.all()
    serializer = LibraryResourceSerializer(resources, many=True)
    return Response({'results': serializer.data})
