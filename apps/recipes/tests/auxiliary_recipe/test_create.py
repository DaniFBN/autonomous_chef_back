from django.test import TestCase
from model_bakery import baker
from apps.recipes.classes.auxiliary_recipe_model import AuxiliaryRecipe


class CreateAuxiliaryRecipeTestCase(TestCase):

    def setUp(self):
        packaging = baker.make('recipes.RecipePackaging')
        recipe = baker.make('recipes.Recipe', yields=2, packaging=packaging)
        for i in range(1, 6):
            # Amount will be between 100 and 600
            amount = int(f'{i}00')

            # Price will be between 1 and 125
            price = i ** 3

            # Create an 'Ingredient' with this 'amount' and 'price'
            ing = baker.make('storage.Ingredient', amount=amount, price=price)
            
            # Create a 'Packaging' with this 'amount' and 'price'
            pack = baker.make('storage.Packaging', amount=i, price=price)
            
            # Add this pack in a RecipePackaging
            packaging.packaging.add(pack)

            # Create a 'RecipeIngredient' with this 'amount'
            recipe_ingredient = baker.make(
                'recipes.RecipeIngredient', ingredient=ing, amount=amount)

            # Add this 'Ingredient' in a recipe
            recipe.items.add(recipe_ingredient)
            
            

        self.data = { 'recipe': recipe }
            

    def test_create_success(self):
        response = AuxiliaryRecipe.create(self.data)

        self.assertIn('id', response.__dict__)
        self.assertEqual(response.cost, 280)
        self.assertEqual(response.portion_cost, 140)
