from django.db import models


class AuxiliaryRecipe(models.Model):
    # An auxiliary table to FK instead of make self reference without FK
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE)
    
    @classmethod
    def create(cls, data):
        ''' data = { recipe: Recipe }'''
        obj = cls(**data)
        obj.save()
        
        return obj
    
    @property
    def cost(self):
        return self.recipe.cost
    
    @property
    def portion_cost(self):
        return self.recipe.portion_cost