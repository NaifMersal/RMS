from django.db import models
from django.contrib.auth.models import User

# class User(AbstractUser):
#     USERNAME_FIELD = 'email'
#     email = models.EmailField(('email address'), unique=True) # changes email to unique and blank to false
#     REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS

class Author(models.Model):
    name=models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    category=models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.category

# class UserProfile(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)



class Refrence(models.Model):
    title=models.CharField(max_length=256)
    location=models.TextField()
    description=models.TextField()
    author=models.ForeignKey(Author, on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)

    def __str__(self):
        return self.title




    


