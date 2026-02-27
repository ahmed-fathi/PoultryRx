from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import PublicProfileSerializer


@api_view(['GET'])
def public_profile(request, username):
    try:
        profile = UserProfile.objects.select_related('user').get(user__username=username)
    except UserProfile.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = PublicProfileSerializer(profile)
    return Response(serializer.data)
