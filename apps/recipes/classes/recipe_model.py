from django.db import models
from apps.recipes.classes.auxiliary_recipe_model import AuxiliaryRecipe

from apps.recipes.classes.recipe_ingredient_model import RecipeIngredient
from apps.recipes.classes.recipe_packaging_model import RecipePackaging
from apps.recipes.utils.enums.recipe_type import RecipeType

_CONSTRAINTS = {
    'name': 'recipe_recipe_type_valid',
    'check': models.Q(recipe_type__in=RecipeType.valid_values())
}


class Recipe(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, null=True)

    # Split recipes in groups easier
    recipe_type = models.PositiveSmallIntegerField(
        choices=RecipeType.choices(), default=RecipeType.Default
    )

    # All ingredients to make recipe
    items = models.ManyToManyField(RecipeIngredient)

    # Recipe used in this recipe.
    # For example: Gingerbread cake is used in Gingerbread
    ancillary_recipes = models.ManyToManyField(
        AuxiliaryRecipe, related_name='ancillary_recipes')

    # A set of packaging
    packaging = models.OneToOneField(
        RecipePackaging, on_delete=models.CASCADE, null=True)

    # How much does this recipe yield
    yields = models.PositiveSmallIntegerField(default=1)

    class Meta:
        constraints = (models.CheckConstraint(**_CONSTRAINTS),)

    @classmethod
    def create(cls, data):
        ''' 
        data = { 
            name, recipe_type, yields, items: RecipeIngredient[2], 
            description?, packaging?: Packaging[], ancillary_recipes?: AuxiliarRecipe[]
        }
        '''
        items = data.pop('items')
        packaging = None
        ancillary_recipes = None

        if 'packaging' in data:
            packaging = data.pop('packaging')

        if 'ancillary_recipes' in data:
            ancillary_recipes = data.pop('ancillary_recipes')

        obj = cls(**data)
        obj.save()

        obj.__add_items(items)
        if packaging:
            obj.__add_packaging(packaging)

        if ancillary_recipes:
            obj.__add_ancillary_recipes(ancillary_recipes)

        return obj

    @property
    def cost(self):
        items = self.items.all()
        packaging = self.packaging
        ancillary_recipes = self.ancillary_recipes.all()

        final_cost = 0.0
        for i in [*items, *ancillary_recipes]:
            final_cost += i.price

        if packaging:
            final_cost += packaging.price

        return round(final_cost, 2)

    @property
    def portion_cost(self):
        cost = self.cost
        portion_cost = cost / self.yields

        return portion_cost

    def __add_items(self, values):
        for value in values:
            self.items.add(value)

    def __add_packaging(self, values):
        packaging = RecipePackaging.create({'packaging': values})
        self.packaging = packaging
        self.save()

    def __add_ancillary_recipes(self, values):
        for value in values:
            aux = AuxiliaryRecipe.create({'recipe': value})
            self.ancillary_recipes.add(aux)
