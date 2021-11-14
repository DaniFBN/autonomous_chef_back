from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.recipes.classes.price_list_model import PriceList


class SaleRecipe(models.Model):
    """ Contains a recipe and values to control price and profit of sale """

    recipe = models.ForeignKey(PriceList, on_delete=models.PROTECT)

    # Amount of recipes sold
    amount = models.PositiveSmallIntegerField(default=1)

    # Cost of an item of this sale
    item_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                    validators=[MinValueValidator(0.01)]
                                    )

    # Price of an item of this sale
    item_price = models.DecimalField(max_digits=6, decimal_places=2,
                                     validators=[MinValueValidator(0.01)]
                                     )

    # Discount to apply in this recipe
    discount = models.PositiveSmallIntegerField(null=True,
                                                validators=[
                                                    MaxValueValidator(100)]
                                                )

    @classmethod
    def create(cls, data):
        """ data = { recipe: PriceList, amount, item_price?, discount? } """
        obj = cls(**data)
        obj.item_cost = obj.recipe.cost

        if not obj.item_price:
            obj.item_price = obj.recipe.price

        obj.save()

        return obj

    @property
    def price(self):
        """ Calculate the price with discount of this sale """
        price = float(self.item_price * self.amount)

        discount = self.__calc_discount(price)

        final_price = price - discount
        return round(final_price, 2)

    @property
    def profit(self):
        """ Calculate the profit of this sale """
        return self.price - self.__calc_cost()

    @property
    def profit_percentage(self):
        """ How much percentage of profit """
        x = self.__calc_cost() * 100
        profit_percentage = x / float(self.price)

        return profit_percentage

    def __calc_discount(self, price):
        """ Calculate the discount value, if dont have discount, return 0 """
        if not self.discount:
            return 0.0

        discount = float(price) * (self.discount / 100)
        return round(discount, 2)

    def __calc_cost(self):
        """ Calculate the cost of the entire sale """
        return float(round(self.item_cost * self.amount, 2))
