from graphene import ObjectType

from apps.storage.api.graphql.mutations.ingredient_mutation import IngredientCreateMutation,IngredientUpdateMutation


class Mutations(ObjectType):
    add_ingredient = IngredientCreateMutation.Field()
    update_ingredient = IngredientUpdateMutation.Field()
    # create_or_update_packaging = PackagingMutation.Field()
