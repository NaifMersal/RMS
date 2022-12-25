from rest_framework import serializers
from . import models


class Author(serializers.ModelSerializer):

    class Meta:
        model= models.Author
        fields=['name']



class Category(serializers.ModelSerializer):

    class Meta:
        model= models.Category
        fields=['category']

# class UserProfile(serializers.ModelSerializer):
    



class Refrence(serializers.ModelSerializer):

    class Meta:
        model= models.Refrence
        fields='__all__'
        extra_kwargs = {'password': {'write_only': True}}
        #read_only_fields = ['account_name']