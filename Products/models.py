from django.db import models
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
