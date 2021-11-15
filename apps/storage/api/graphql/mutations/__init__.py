from graphene import ObjectType

from apps.storage.api.graphql.mutations.ingredient_mutations import IngredientCreateMutation, IngredientUpdateMutation, IngredientDeleteMutation
from apps.storage.api.graphql.mutations.packaging_mutations import PackagingCreateMutation, PackagingUpdateMutation, PackagingDeleteMutation


class Mutations(ObjectType):
    # Ingredients
    add_ingredient = IngredientCreateMutation.Field()
    update_ingredient = IngredientUpdateMutation.Field()
    delete_ingredient = IngredientDeleteMutation.Field()

    # Packaging
    add_packaging = PackagingCreateMutation.Field()
    update_packaging = PackagingUpdateMutation.Field()
    delete_packaging = PackagingDeleteMutation.Field()
