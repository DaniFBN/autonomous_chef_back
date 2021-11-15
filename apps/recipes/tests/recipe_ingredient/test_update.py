from django.test import TestCase
from model_bakery import baker
from apps.recipes.classes.recipe_ingredient_model import RecipeIngredient


class UpdateRecipeIngredientTestCase(TestCase):

    def setUp(self):
        baker.make('recipes.RecipeIngredient')

        self.data = {'amount': 124}

    def test_create_success(self):
        old = RecipeIngredient.objects.get(id=1)
        
        new = RecipeIngredient.objects.get(id=1)
        new.update(self.data)

        self.assertNotEqual(old.amount, new.amount)
        self.assertTrue(new.amount, self.data.get('amount'))
