from django.test import TestCase

from model_bakery import baker

from core.classes.ingredient_model import Ingredient


class UpdateIngredientTestCase(TestCase):

    def setUp(self):
        baker.make('core.Ingredient')
        
        self.data = baker.prepare('core.Ingredient').__dict__

    def test_update_success(self):
        old = Ingredient.objects.get(id=1)
        
        new = Ingredient.objects.get(id=1)
        new.update(self.data)

        self.assertEqual(old.id, new.id)
        self.assertNotEqual(old.name, new.name)
        self.assertNotEqual(old.amount, new.amount)
        self.assertNotEqual(old.price, new.price)
