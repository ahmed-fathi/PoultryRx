from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FAQEntry
from .serializers import FAQEntrySerializer


@api_view(['GET'])
def faq_list(request):
    entries = FAQEntry.objects.all()
    serializer = FAQEntrySerializer(entries, many=True)
    return Response({'results': serializer.data})
