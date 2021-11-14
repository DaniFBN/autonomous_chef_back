from django.db import models
from django.utils import timezone

from apps.sales.classes.sale_recipe_model import SaleRecipe


class Sale(models.Model):
    """ A set of SaleRecipe with date and computed price """

    # A set of recipes with their prices and costs
    recipes = models.ManyToManyField(SaleRecipe)

    # Current date of sale
    date = models.DateField(default=timezone.now, editable=False)

    @classmethod
    def create(cls, data):
        """ data = { recipes: SaleRecipe[] } """
        obj = cls()
        obj.save()

        obj.__add_recipes(data.get('recipes'))

        return obj

    def __add_recipes(self, recipes):
        for recipe in recipes:
            self.recipes.add(recipe)

    @property
    def price(self):
        """ Sum the price of all recipes """
        recipes = self.__all_recipes()

        price = 0.0
        for recipe in recipes:
            price += recipe.price

        return round(price, 2)

    @property
    def profit(self):
        """ Sum the profit of all recipes """
        recipes = self.__all_recipes()

        profit = 0.0
        for recipe in recipes:
            profit += recipe.profit

        return round(profit, 2)

    def __all_recipes(self):
        return self.recipes.all()
