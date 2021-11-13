from django.db import models
from apps.sales.classes.auxiliary_recipe_model import AuxiliaryRecipe

from apps.sales.classes.recipe_ingredient_model import RecipeIngredient
from apps.sales.classes.recipe_packaging_model import RecipePackaging
from apps.sales.utils.enums.recipe_type import RecipeType

_CONSTRAINTS = {
    'name': 'recipe_recipe_type_valid',
    'check': models.Q(recipe_type__in=RecipeType.valid_values())
}


class Recipe(models.Model):
    name = models.CharField(max_length=50, unique=True)
    recipe_type = models.PositiveSmallIntegerField(
        choices=RecipeType.choices(), default=RecipeType.Default
    )
    description = models.CharField(max_length=100, null=True)
    items = models.ManyToManyField(RecipeIngredient)
    ancillary_recipes = models.ManyToManyField(
        AuxiliaryRecipe, related_name='ancillary_recipes')
    packagins = models.ManyToManyField(RecipePackaging)
    yields = models.PositiveSmallIntegerField(default=1)

    class Meta:
        constraints = (models.CheckConstraint(**_CONSTRAINTS),)

    def recipe_price(self):
        items = self.items.all()
        packagins = self.packagins.all()
        recipes = self.recipes.all()

        final_price = 0.0
        for i in [*items, *packagins, *recipes]:
            final_price += i.price

        return final_price

    def portion_price(self):
        price = self.recipe_price()
        portion_price = price / self.yields

        return portion_price
