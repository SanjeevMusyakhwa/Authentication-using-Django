from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
  full_name = models.CharField(max_length=255)
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=20,unique=True)
  
  
  USERNAME_FIELD ='phone_number'
  REQUIRED_FIELDS = ['full_name', 'username', 'email']
  
  def __str__(self):
        return f"{self.full_name} ({self.username}) - {self.phone_number}"
