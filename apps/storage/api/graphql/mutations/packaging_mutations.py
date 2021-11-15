import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

from apps.storage.api.rest.packaging.all_serializer import PackagingAllSerializer
from apps.storage.api.rest.packaging.update_serializer import PackagingUpdateSerializer
from apps.storage.classes.packaging_model import Packaging


class PackagingCreateMutation(SerializerMutation):

    class Meta:
        serializer_class = PackagingAllSerializer
        model_operations = ('create')


class PackagingUpdateMutation(SerializerMutation):

    class Meta:
        serializer_class = PackagingUpdateSerializer
        model_operations = ('update')


class PackagingDeleteMutation(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, **kwargs):
        ok = False

        id = kwargs.get('id')
        obj = Packaging.get_by_id(id)
        if obj:
            obj.delete()
            ok = True

        return PackagingDeleteMutation(ok=ok)
