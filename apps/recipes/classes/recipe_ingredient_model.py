from django.db import models

from apps.storage.classes.ingredient_model import Ingredient


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    # Amount of ingredient, to get price_cost to this recipe
    amount = models.PositiveSmallIntegerField()

    @classmethod
    def create(cls, data):
        ''' data = { ingredient: Ingredient, amount}'''
        obj = cls(**data)
        obj.save()

        return obj

    def update(self, data):
        ''' data = { amount}'''
        self.amount = data.get('amount')
        self.save()

        return self

    @property
    def price(self):
        ingredient_price = float(self.ingredient.price)
        ingredient_amount = self.ingredient.amount

        recipe_amount = self.amount

        multiplier = recipe_amount / ingredient_amount

        final_price = ingredient_price * round(multiplier, 2)
        return round(final_price, 2)
