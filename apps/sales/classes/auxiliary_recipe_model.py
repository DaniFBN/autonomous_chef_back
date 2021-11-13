from django.db import models


class AuxiliaryRecipe(models.Model):
    recipe = models.ForeignKey('sales.Recipe', on_delete=models.CASCADE)