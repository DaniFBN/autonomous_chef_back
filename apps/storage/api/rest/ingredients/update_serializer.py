from rest_framework import serializers

from apps.storage.classes.ingredient_model import Ingredient


class IngredientUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'description',
            'amount',
            'price'
        )
        
    def update(self, instance, validated_data):
        return instance.update(validated_data)
