from django.db import models


class Packaging(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
