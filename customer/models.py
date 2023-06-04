from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
# Create your models here.


class Customer(AbstractUser):
    phone_number = models.CharField(default='', max_length=15)
    address = models.CharField(default='', max_length=255)


