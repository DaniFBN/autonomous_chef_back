from django.test import TestCase
from model_bakery import baker
from apps.recipes.classes.recipe_model import Recipe

from apps.recipes.utils.enums.recipe_type import RecipeType


class CreateRecipeTestCase(TestCase):

    def setUp(self):
        data = {
            'name': 'Basic Recipe',
            'description': 'Desc',
            'recipe_type': RecipeType.Cake,
            'yields': 5,
            'packaging': [],
            'items': [],
        }

        for i in range(0, 3):
            pack = baker.make('storage.Packaging')
            ingredient = baker.make('recipes.RecipeIngredient')

            data['packaging'].append(pack)
            data['items'].append(ingredient)

        self.base_data = data

        ancillary_recipes = baker.make(
            'recipes.Recipe', make_m2m=True, _quantity=2)
        self.recipes_data = {
            **self.base_data,
            'ancillary_recipes': ancillary_recipes
        }

    def test_create_base_success(self):
        response = Recipe.create(self.base_data.copy())

        self.assertIn('id', response.__dict__)
        self.assertEqual(self.base_data.get('name'), response.name)
        self.assertEqual(
            self.base_data.get('description'), response.description
        )
        self.assertEqual(self.base_data.get('yields'), response.yields)
        self.assertEqual(
            self.base_data.get('recipe_type'), response.recipe_type
        )

        packaging = response.packaging.packaging.all()
        for pack in self.base_data.get('packaging'):
            self.assertIn(pack, packaging)

        items = response.items.all()
        for item in self.base_data.get('items'):
            self.assertIn(item, items)

    def test_create_recipes_success(self):
        response = Recipe.create(self.recipes_data.copy())

        ancillarys = response.ancillary_recipes.all()
        for recipe in self.recipes_data.get('ancillary_recipes'):
            self.assertGreater(len(ancillarys.filter(recipe=recipe)), 0)
