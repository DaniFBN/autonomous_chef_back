from django.db import models
from django.utils import timezone

from apps.sales.classes.sale_recipe_model import SaleRecipe


class Sale(models.Model):
    """ A set of SaleRecipe with date and computed price """
    
    # A set of recipes with their prices and costs
    recipes = models.ManyToManyField(SaleRecipe)
    
    # Current date of sale
    date = models.DateField(default=timezone.now)
    
    @property
    def price(self):
        """ Sum the price of all recipes """
        recipes = self.__all_recipes()
        
        price = 0.0
        for recipe in recipes:
            price += recipe.price
            
        return price   
    
    @property
    def profit(self):
        """ Sum the profit of all recipes """
        recipes = self.__all_recipes()
        
        profit = 0.0
        for recipe in recipes:
            profit += recipe.profit
            
        return profit  
        
        
    def __all_recipes(self):
        return self.recipes.all()         
