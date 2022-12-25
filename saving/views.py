from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from . import models, serializer 


# Create your views here.
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def get_post_refrences(request):

    if request.method=='GET':
        print(request.data)
        refrences= models.Refrence.objects.filter(user=request.user).all()
        ser_ref= serializer.Refrence(refrences, many=True)
        return Response(ser_ref.data)
    
    if request.method=='POST':
        refrence=models.Refrence(data=request.data)
        if(refrence.is_valid()):
            return Response(refrence.validate_data, status=status.HTTP_201_CREATED)
    
    return Response(refrence.errors, status=status.HTTP_400_BAD_REQUEST)






    

