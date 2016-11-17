from django.db import models

class Products(models.Model):
    name = models.CharField(max_lenght=255)
    description = models.CharField(max_lenght=255)
    category = models.CharField(max_lenght=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
