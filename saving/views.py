from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from . import models, serializer 


# Create your views here.
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST','DELETE', 'PUT'])
def CURD_refrences(request):
    
    if request.method=='GET':

        refrences= models.Refrence.objects.filter(user=request.user.id).all()
        ser_ref= serializer.RefrenceSerializer(refrences, many=True)
        return Response(ser_ref.data)
    
    if request.method=='POST':

        # data={ "title":request.data['title'],"location":request.data['location'] , "user":request.user}
        print(request.data)
        refrence=serializer.RefrenceSerializer(data=request.data)
        if(refrence.is_valid()):
            print(refrence.validated_data)
            re=refrence.create(refrence.validated_data, request.user)
            return Response(refrence.validated_data, status=status.HTTP_201_CREATED)

    if request.method=='DELETE':
        refrence=models.Refrence.objects.get(user=request.user.id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    if request.method=='PUT':
        data={ **request.data , "user":request.user.id}
        refrence= serializer.RefrenceSerializer(data=data)
        if(refrence.is_valid()):
            refrence.save()
            return Response(refrence.validated_data, status=status.HTTP_201_CREATED)
    
    return Response(refrence.errors, status=status.HTTP_400_BAD_REQUEST)










    

