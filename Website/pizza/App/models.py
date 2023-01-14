from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class user_extra(models.Model):
    full_name = models.CharField(max_length=120)
    phone_no = models.CharField(max_length=10)
    Date_of_birth = models.DateField()
    user_address1 = models.TextField()
    user_address2 = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    Countary = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class menu1(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='menu/image')
    price = models.IntegerField()


class contact1(models.Model):
    contact_name = models.CharField(max_length=150, null=True)
    contact_email = models.EmailField(max_length=150, null=True)
    contact_message = models.TextField(null=True)
