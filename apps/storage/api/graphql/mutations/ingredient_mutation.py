import graphene

from apps.storage.api.graphql.object_types import IngredientType
from apps.storage.classes.ingredient_model import Ingredient
from apps.storage.utils.enums.unit_measurement import UnitMeasurement


def obj_to_dict(value):
    response = value.__dict__
    response.pop('_state')
    return response


class IngredientCreateMutation(graphene.Mutation):
    Output = IngredientType

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        unit_measurement = graphene.NonNull(
            graphene.Enum.from_enum(UnitMeasurement)
        )
        amount = graphene.Int(required=True)
        price = graphene.Float(required=True)

    def mutate(self, info, **kwargs):
        obj = Ingredient.create(kwargs)
        return IngredientType(**obj_to_dict(obj))


class IngredientUpdateMutation(graphene.Mutation):
    Output = IngredientType

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        description = graphene.String()
        amount = graphene.Int(required=True)
        price = graphene.Float(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs.get('id')        
        obj = Ingredient.get_by_id(id)
        obj.update(kwargs)
        
        return IngredientType(**obj_to_dict(obj))
