from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.recipes.classes.recipe_model import Recipe


class SaleRecipe(models.Model):
    """ Contains a recipe and values to control price and profit of sale """
    
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    
    # Amount of recipes sold
    amount = models.PositiveSmallIntegerField(default=1)
    
    # Cost of an item of this sale
    item_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                    validators=[MinValueValidator(0.01)]
                                    )
    
    # Price of an item of this sale
    item_value = models.DecimalField(max_digits=6, decimal_places=2,
                                     validators=[MinValueValidator(0.01)]
                                     )

    # Discount to apply in this recipe
    discount = models.PositiveSmallIntegerField(null=True,
                                                validators=[
                                                    MaxValueValidator(100)]
                                                )

    @property
    def price(self):
        """ Calculate the price with discount of this sale """
        price = self.item_value * self.amount

        discount = self.__calc_discount(price)

        final_price = price - discount
        return final_price

    @property
    def profit(self):
        """ Calculate the profit of this sale """
        final_cost = self.__calc_cost()

        return self.price - final_cost

    @property
    def profit_percentage(self):
        """ How much percentage of profit """
        x = self.__calc_cost() * 100
        profit_percentage = x / self.price

        return profit_percentage

    def __calc_discount(self, price):
        """ Calculate the discount value, if dont have discount, return 0 """
        if not self.discount: return 0.0
        
        discount = price * (self.discount / 100)
        return round(discount, 2)

    def __calc_cost(self):
        """ Calculate the cost of the entire sale """
        return self.item_cost * self.amount
