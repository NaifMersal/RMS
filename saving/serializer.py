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
    


    class Meta:
        model= models.Refrence
        exclude=['user']
        depth=1


    def create(self, validated_data, user_id, categories_data=None):
        data={ **validated_data, "user": user_id}
        refrence=models.Refrence.objects.create(**data)
        print(categories_data)
        if(categories_data is not None):
            for category in categories_data:
                refrence.categories.add(models.Category.objects.get_or_create(tag=category)[0])
    
    def update(self, instance, validated_data, categories_data=None):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if(categories_data is not None):
            for category in instance.categories.all():
                for i,tag in enumerate(categories_data):
                    if(category.tag==tag):
                        category.tag = categories_data.pop(i)
        

        if(categories_data is not None):
            for category in categories_data:
                instance.categories.add(models.Category.objects.get_or_create(tag=category)[0])
        
        instance.save()
        return instance




