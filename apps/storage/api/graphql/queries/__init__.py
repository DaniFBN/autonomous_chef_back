from apps.storage.api.graphql.queries.ingredient_query import IngredientQuery
from apps.storage.api.graphql.queries.packaging_query import PackagingQuery


class QueryDefinition(IngredientQuery, PackagingQuery):
    pass
