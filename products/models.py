from django.db import models
from django.conf import settings



class Product(models.Model):
     name = models.CharField(max_length=255)
     price = models.FloatField()
     stock = models.IntegerField()
     image_url= models.CharField(max_length=2083)





