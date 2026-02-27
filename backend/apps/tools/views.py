from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tool
from .serializers import ToolSerializer


@api_view(['GET'])
def tools_list(request):
    tools = Tool.objects.all()
    serializer = ToolSerializer(tools, many=True)
    return Response({'results': serializer.data})
