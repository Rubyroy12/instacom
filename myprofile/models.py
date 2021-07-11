from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username


class Comments(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField()

class UpdateProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio=models.TextField()
    tags = models.ManyToManyField(tags,blank=True)
    modified=models.DateTimeField(auto_now_add=True)
    profile_pic= CloudinaryField('image')

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self): #will return the string rep of our models 
        return self.name