from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Offer(models.Model):
    discount = models.FloatField()
    discription = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
