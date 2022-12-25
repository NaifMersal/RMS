from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import  AllowAny
from . import serializer
from rest_framework import status


# class CustomAuthToken(ObtainAuthToken):
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         user_serializer = serializer.UserSerializer(data=request.data,
#                                            context={'request': request})
#         user_serializer.is_valid(raise_exception=True)
#         user = user_serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#         })

@permission_classes([AllowAny])
@api_view(['POST'])
def regster(request):
    if request.method == 'POST':
        user_serializer=serializer.UserSerializer(data=request.data)
        if(user_serializer.is_valid()):
            user=user_serializer.create(user_serializer.validated_data)
            token=Token.objects.create(user=user)
            return Response({'token': token.key})

    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

