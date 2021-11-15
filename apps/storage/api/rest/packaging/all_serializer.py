from rest_framework import serializers

from apps.storage.classes.packaging_model import Packaging


class PackagingAllSerializer(serializers.ModelSerializer):
    unit_measurement = serializers.IntegerField()

    class Meta:
        model = Packaging
        fields = (
            'id',
            'name',
            'description',
            'unit_measurement',
            'amount',
            'price'
        )

    def create(self, validated_data):
        return super().create(validated_data)
