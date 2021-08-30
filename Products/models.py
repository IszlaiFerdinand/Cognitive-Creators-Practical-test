from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)


class Brand(models.Model):
    name = models.CharField(max_length=150)


class Product(models.Model):
    name = models.CharField(max_length=150)
    onstock = models.IntegerField()
    season = models.CharField(max_length=150)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,)
    img = models.ImageField(upload_to='Pictures')
    size = models.CharField(max_length=150)


class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    quantity = models.IntegerField()
    user = models.ForeignKey(User,  on_delete=models.CASCADE,)
    ordered = models.BooleanField(default=False)


class Order(models.Model):
    usertype = models.CharField(max_length=150)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    adress = models.CharField(max_length=500)
    iban = models.CharField(max_length=150)
    bank = models.CharField(max_length=150)
    registrationnumber = models.CharField(max_length=150)
    delivery = models.CharField(max_length=150)
    payment = models.CharField(max_length=150)
    comments = models.CharField(max_length=150)
    totalamount = models.FloatField(default=0)
