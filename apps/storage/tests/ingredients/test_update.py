from django.test import TestCase
from model_bakery import baker

from apps.storage.classes.ingredient_model import Ingredient


class UpdateIngredientTestCase(TestCase):

    def setUp(self):
        baker.make('storage.Ingredient', description='Desc')

        self.data = baker.prepare('storage.Ingredient',
                                  description='Desc').__dict__

    def test_update_success(self):
        old = Ingredient.objects.get(id=1)

        new = Ingredient.objects.get(id=1)
        new.update(self.data)

        self.assertEqual(old.id, new.id)
        self.assertNotEqual(old.name, new.name)
        self.assertNotEqual(old.amount, new.amount)
        self.assertNotEqual(old.price, new.price)

    def test_update_success_description(self):
        new = Ingredient.objects.get(id=1)
        self.data.pop('description')
        new.update(self.data)

        self.assertEqual(new.description, None)
