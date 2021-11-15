from django.test import TestCase

from apps.storage.classes.ingredient_model import Ingredient
from apps.storage.utils.enums.unit_measurement import UnitMeasurement


class CreateIngredientTestCase(TestCase):

    def setUp(self):
        self.data = {
            'name': 'Egg',
            'description': 'Pack with 12',
            'unit_measurement': UnitMeasurement.Unity,
            'amount': 12,
            'price': 9.0
        }

    def test_create_success(self):
        response = Ingredient.create(self.data)

        self.assertIn('id', response.__dict__)
