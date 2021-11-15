from graphene import ObjectType, Schema

from apps.storage.api.graphql.query import QueryDefinition
from apps.storage.api.graphql.mutations import Mutations


class Query(QueryDefinition, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutations)
