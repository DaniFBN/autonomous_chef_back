from django.db import models

from apps.recipes.classes.recipe_model import Recipe


class SaleRecipe(models.Model):
    recipes = models.ManyToManyField(Recipe)
    amount = models.PositiveSmallIntegerField(default=1)
    item_value = models.DecimalField(max_digits=6, decimal_places=2)
