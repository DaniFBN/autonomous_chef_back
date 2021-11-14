from django.test import TestCase
from model_bakery import baker
from apps.recipes.classes.recipe_packaging_model import RecipePackaging


class UpdateRecipePackagingTestCase(TestCase):

    def setUp(self):
        new_packaging = baker.make('storage.Packaging', _quantity=3)
        obj = baker.make('recipes.RecipePackaging', make_m2m=True)
        current_packaging = obj.packaging.all()[:2]

        self.data = { 'packaging': [*new_packaging, *current_packaging] }
            

    def test_update_success(self):       
        new = RecipePackaging.objects.get(id=1)
        new.update(self.data)

        packaging = new.packaging.all()
        self.assertEqual(len(packaging), 5)
        
        for pack in packaging:
            self.assertIn(pack, self.data.get('packaging'))
