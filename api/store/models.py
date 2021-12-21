from django.db import models
from django.db.models.aggregates import Max

# Create your models here.

class Product(models.Model):
    id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name