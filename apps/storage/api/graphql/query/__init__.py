from apps.storage.api.graphql.query.ingredient_query import IngredientQuery
from apps.storage.api.graphql.query.packaging_query import PackagingQuery


class QueryDefinition(PackagingQuery, IngredientQuery):
    pass
