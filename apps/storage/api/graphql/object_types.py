from graphene_django.types import DjangoObjectType

from apps.storage.classes.ingredient_model import Ingredient
from apps.storage.classes.packaging_model import Packaging


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class PackagingType(DjangoObjectType):
    class Meta:
        model = Packaging
