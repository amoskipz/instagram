from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image, Profile, Comment


# Create your tests here.


class ProfileTescase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('amos')
        cls.profile = Profile(profile_pic='', bio ='Brought up in Kenya',user=cls.user)

    def test_instance(cls):
        cls.assertTrue(isinstance(cls.profile, Profile))        

    def save_method_test(self):
        self.profile.save_profile()
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)

class ImageTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user.objects.create_user('amos')
        cls.new_profile = Profile (profile_pic='')    
        cls.new_image = Image(my_image='', caption='Corona', profile=cls.new_profile)

    def test_instance_true(cls):
        cls.assertTrue(isinstance(cls.new_image, Image))

    def test_save_image_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()      
