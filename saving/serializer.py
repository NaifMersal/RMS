from rest_framework import serializers
from . import models



class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model= models.Author
        fields=['name']



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model= models.Category
        fields=['category']

# class UserProfile(serializers.ModelSerializer):
    



class RefrenceSerializer(serializers.ModelSerializer):
    categories=CategorySerializer(many=True, required=False)

    class Meta:
        model= models.Refrence
        exclude=['user']

    
    


    
    def create(self, validated_data, user_id):
        categories_data=validated_data.pop('categories',default=None)
        data={ **validated_data, "user": user_id}
        refrence=models.Refrence.objects.create(**data)
        print(type(categories_data))
        if(categories_data is not None):
            for category in categories_data:
                refrence.categories.add(models.Category.objects.get_or_create(tag=category))

        return refrence




