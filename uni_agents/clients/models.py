from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class University(models.Model):
  name = models.CharField(max_length=200, null=True)
  address = models.CharField(max_length=100, null=True)
  city = models.CharField(max_length=100, null=True)
  state = models.CharField(max_length=100, null=True)
  postal = models.CharField(max_length=100, null=True)
  country = models.CharField(max_length=100, null=True)
  website = models.CharField(max_length=100, null=True)
  email = models.EmailField(max_length=100, null=True)
  description = models.CharField(max_length=500, null=True)
  isono = models.CharField(max_length=100, null=True)
  representative = models.CharField(max_length=100, null=True)
  position = models.CharField(max_length=100, null=True)
  phone = models.CharField(max_length=100, null=True)
  repemail = models.EmailField(max_length=100, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name


class Agent(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  bio = models.CharField(max_length=200, null=True)
  nationality = models.CharField(max_length=100, null=True)
  national_id = models.CharField(max_length=20, null=True)
  location = models.CharField(max_length=100, null=True)
  birth_date = models.DateField(null=True)
  phone = models.CharField(max_length=100, null=True)
  profile_pic = models.ImageField(default="default_profile.jpg", null=True, blank=True)
  is_active = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.first_name


class Contact(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  message = models.CharField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name


class Subscribe(models.Model):
  email = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.email