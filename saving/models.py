from django.db import models
from django.contrib.auth.models import User

# class User(AbstractUser):
#     USERNAME_FIELD = 'email'
#     email = models.EmailField(('email address'), unique=True) # changes email to unique and blank to false
#     REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS

class Author(models.Model):
    name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    tag=models.CharField(default='unknown',max_length=50)
    
    


    def __str__(self):
        return self.tag

    def get_unkown():
        return Category.objects.get_or_create(tag='unknown')
    


# class UserProfile(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)







class Refrence(models.Model):
    title=models.CharField(max_length=256)
    location=models.TextField()
    description=models.TextField(null=True)
    author=models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    categories=models.ManyToManyField(Category, default=Category.get_unkown)


    def __str__(self):
        return self.title




    


