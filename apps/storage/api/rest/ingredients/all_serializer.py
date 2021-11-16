from rest_framework import serializers

from apps.storage.classes.ingredient_model import Ingredient


class IngredientAllSerializer(serializers.ModelSerializer):
    unit_measurement = serializers.IntegerField()

    class Meta:
        model = Ingredient
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

    def is_valid(self, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
