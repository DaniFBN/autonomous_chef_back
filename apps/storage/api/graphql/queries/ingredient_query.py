import graphene

from apps.storage.api.graphql.object_types import IngredientType
from apps.storage.classes.ingredient_model import Ingredient


class IngredientQuery:
    all_ingredients = graphene.List(IngredientType)

    def resolve_all_ingredients(self, into, **kwargs):
        return Ingredient.objects.all()
