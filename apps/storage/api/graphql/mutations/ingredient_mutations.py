import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

from apps.storage.api.rest.ingredients.all_serializer import IngredientAllSerializer
from apps.storage.api.rest.ingredients.update_serializer import IngredientUpdateSerializer
from apps.storage.classes.ingredient_model import Ingredient


class IngredientCreateMutation(SerializerMutation):

    class Meta:
        serializer_class = IngredientAllSerializer
        model_operations = ('create')


class IngredientUpdateMutation(SerializerMutation):

    class Meta:
        serializer_class = IngredientUpdateSerializer
        model_operations = ('update')


class IngredientDeleteMutation(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, **kwargs):
        ok = False

        id = kwargs.get('id')
        obj = Ingredient.get_by_id(id)
        if obj:
            obj.delete()
            ok = True

        return IngredientDeleteMutation(ok=ok)
