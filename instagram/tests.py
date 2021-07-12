from django.test import TestCase
from .models import Profile, Image
from django.contrib.auth.models import User


class ProfileTestClass(TestCase):
    from django.contrib.auth.models import User
    def setUp(self):
        self.user = User(username='martin')
        self.user.save()
        self.profile = Profile(id=1,user=self.user,photo='download.jpeg',bio='My name is Martin', name='person')
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)


class ImageTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user=User(username='martin'))
        self.profile.user.save()
        self.profile.save()
        self.image = Image(user=self.profile,image='download.jpeg', name='person', caption='this is it')
        self.image.save_image()

    def test_insatance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_update_image_caption(self):
        self.image.save_image()
        new_caption =Image.update_image('this is it','Yeah')
        image = Image.objects.get(caption='Yeah')
        self.assertEqual(image.caption,'Yeah')