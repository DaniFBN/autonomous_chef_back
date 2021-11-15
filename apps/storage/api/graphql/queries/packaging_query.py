import graphene

from apps.storage.api.graphql.object_types import PackagingType
from apps.storage.classes.packaging_model import Packaging


class PackagingQuery:
    all_packaging = graphene.List(PackagingType)

    def resolve_all_packaging(self, into, **kwargs):
        return Packaging.objects.all()
