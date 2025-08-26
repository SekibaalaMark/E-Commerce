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
    

class Product(models.Model):
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=30)
    stock = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    buying_price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)




class Sale(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    


class Expense(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    expense_amount = models.DecimalField()
    date = models.DateTimeField(auto_now_add=True)




