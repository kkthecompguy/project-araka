from django.db import models

# Create your models here.
class University(models.Model):
  name = models.CharField(max_length=200, null=True)
  address = models.CharField(max_length=100, null=True)
  city = models.CharField(max_length=100, null=True)
  state = models.CharField(max_length=100, null=True)
  postal = models.CharField(max_length=100, null=True)
  website = models.CharField(max_length=100, null=True)
  email = models.EmailField(max_length=100, null=True)
  description = models.CharField(max_length=500, null=True)
  representative = models.CharField(max_length=100, null=True)
  postion = models.CharField(max_length=100, null=True)
  phone = models.CharField(max_length=100, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name