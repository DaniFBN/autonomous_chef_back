from django.db import models
from django.utils import timezone

from apps.sales.classes.sale_recipe_model import SaleRecipe


class Sale(models.Model):
    recipes = models.ManyToManyField(SaleRecipe)
    date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=6, decimal_places=2)
