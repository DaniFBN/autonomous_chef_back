from django.test import TestCase
from model_bakery import baker
from apps.recipes.classes.recipe_ingredient_model import RecipeIngredient


class CreateRecipeIngredientTestCase(TestCase):

    def setUp(self):
        amount = 30
        price = 77.23

        obj = baker.make('storage.Ingredient', amount=amount, price=price)

        self.data = {'ingredient': obj, 'amount': 90}

    def test_create_success(self):
        response = RecipeIngredient.create(self.data)

        self.assertIn('id', response.__dict__)
        self.assertEqual(response.price, 77.23 * 3)
