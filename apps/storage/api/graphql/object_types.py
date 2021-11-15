import graphene
from graphene_django.types import DjangoObjectType

from apps.storage.classes.ingredient_model import Ingredient
from apps.storage.classes.packaging_model import Packaging


class IngredientType(DjangoObjectType):
    unit_measurement = graphene.Int()

    class Meta:
        model = Ingredient


class PackagingType(DjangoObjectType):
    unit_measurement = graphene.Int()

    class Meta:
        model = Packaging
