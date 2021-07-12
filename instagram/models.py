from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class Image(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to = 'gallery/', null=True, blank=True)
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=30)

    class Meta:
        ordering = ["-pk"]


    @classmethod
    def images(cls):
        images = cls.objects.all()
        return images

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,old,new):
        cap = Image.objects.filter(caption=old).update(caption=new)
        return cap

    def __str__(self):
        return self.name

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    photo = models.ImageField(upload_to = 'gallery/', null=True, blank=True, default='download.jpeg')
    bio = models.CharField(max_length=300)
    name = models.CharField(blank=True, max_length=120)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def profile(cls):
        profiles = cls.objects.all()
        return profiles

    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def save_profile(self):
        self.user

    def __str__(self):
        return self.name

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='comment')
    photo = models.ForeignKey('Image',on_delete=models.CASCADE,related_name='comment')

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f'{self.user.name} Image'