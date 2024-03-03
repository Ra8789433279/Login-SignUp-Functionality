from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_Patient= models.BooleanField('Is customer', default=False)
    is_Doctor= models.BooleanField('Is employee', default=False)
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    profile_picture = models.ImageField('Profile Picture', upload_to='profile_pictures/', null=True, blank=True)
    address_line1 = models.CharField('Address Line 1', max_length=100, blank=True)
    city = models.CharField('City', max_length=100, default="", blank=True)
    state = models.CharField('State', max_length=100, default="")
    pincode = models.CharField('Pincode', max_length=10)

    def __str__(self):
        return self.username