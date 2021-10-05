from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offers(models.Model):
    discount = models.CharField(max_length=255)
    offer = models.CharField(max_length=255)


