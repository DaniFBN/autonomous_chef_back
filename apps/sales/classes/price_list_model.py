from django.core.validators import MinValueValidator
from django.db import models

from apps.recipes.classes.recipe_model import Recipe

class PriceList(models.Model):
    """ A Price list to remember the standard values """

    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    
    # Sale price with validator to only positive number only
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(0.01)]
                                )

    @property
    def profit(self):
        """ Calculate a profit with current values """
        return self.price - self.recipe.cost

    @property
    def profit_percentage(self):
        """ Calculate a profit percentage with current values """
        x = self.recipe.cost * 100
        profit_percentage = x / self.price

        return profit_percentage
