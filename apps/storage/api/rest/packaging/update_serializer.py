from rest_framework import serializers

from apps.storage.classes.packaging_model import Packaging


class PackagingUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Packaging
        fields = (
            'id',
            'name',
            'description',
            'amount',
            'price'
        )

    def update(self, instance, validated_data):
        return instance.update(validated_data)
