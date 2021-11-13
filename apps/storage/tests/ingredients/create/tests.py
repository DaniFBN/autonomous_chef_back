from django.test import TestCase
from core.classes.ingredient_model import Ingredient
from core.utils.enums.unit_measurement import UnitMeasurement


class CreateIngredientTestCase(TestCase):

    def setUp(self):
        self.data = {
            'name': 'Ovo',
            'description': 'Cartela com 12',
            'unit_measurement': UnitMeasurement.Unity,
            'amount': 12,
            'price': 9.0
        }

    def test_create_success(self):
        response = Ingredient.create(self.data)

        self.assertIn('id', response.__dict__)
