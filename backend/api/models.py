from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    ROLES = [('Admin','Admin'),('cashier','cashier'),('customer','customer')]
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=40,unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10,choices=ROLES)

    def __str__(self):
        return self.username
    



