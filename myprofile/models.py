from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True)
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
    editor= models.ForeignKey(User, on_delete=models.CASCADE)
    bio=models.TextField()
    modified=models.DateTimeField(auto_now_add=True)
    profile_pic= CloudinaryField('image')