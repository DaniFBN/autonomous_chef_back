from django.test import TestCase
from model_bakery import baker
from apps.recipes.classes.recipe_packaging_model import RecipePackaging


class CreateRecipePackagingTestCase(TestCase):

    def setUp(self):
        recipe_packaging = []
        
        # Unit cost = sum of 'i' values
        for i in range(1, 4):
            # Amount will be between 1 and 9
            amount = i ** 2

            # Price will be between 1 and 27
            price = i ** 3

            # Create a 'Packaging' with this 'amount' and 'price'
            obj = baker.make('storage.Packaging', amount=amount, price=price)

            # Add this 'Packaging' in list
            recipe_packaging.append(obj)

        self.data = { 'packaging': recipe_packaging }
            

    def test_create_success(self):
        response = RecipePackaging.create(self.data)

        self.assertIn('id', response.__dict__)
        self.assertEqual(response.price, 6.0)
