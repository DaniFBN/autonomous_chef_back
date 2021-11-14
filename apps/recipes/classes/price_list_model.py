from django.core.validators import MinValueValidator
from django.db import models

from apps.recipes.classes.recipe_model import Recipe


class PriceList(models.Model):
    """ A Price list to remember the standard values """

    recipe = models.ForeignKey(
        Recipe, on_delete=models.PROTECT, editable=False)
    description = models.CharField(max_length=100, null=True)

    # Sale price with validator to only positive number only
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(0.01)]
                                )

    @classmethod
    def create(cls, data):
        """ data = { price : float, recipe: Recipe } """
        obj = cls(**data)
        obj.save()

        return obj

    def update(self, data):
        """ data = { price : float } """
        self.price = data.get('price')

        if 'description' in data:
            self.description = data.get('description')
        elif self.description:
            self.description = None

        self.save()

        return self

    @property
    def cost(self):
        return self.recipe.cost

    @property
    def profit(self):
        """ Calculate a profit with current values """
        return self.price - self.recipe.cost

    @property
    def profit_percentage(self):
        """ Calculate a profit percentage with current values """
        x = self.profit * 100
        profit_percentage = x / self.price

        return profit_percentage
