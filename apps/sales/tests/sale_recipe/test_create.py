from django.test import TestCase
from model_bakery import baker

from apps.sales.classes.sale_recipe_model import SaleRecipe


class CreateSaleRecipeTestCase(TestCase):

    def setUp(self):
        packaging = baker.make('recipes.RecipePackaging', make_m2m=True)
        recipe = baker.make('recipes.Recipe', packaging=packaging)
        price_list = baker.make('recipes.PriceList', recipe=recipe,
                                price=float(recipe.cost) * 2)

        self.data = {'recipe': price_list, 'amount': 2}
        self.discount_data = {**self.data, 'discount': 20}
        self.price_data = {**self.data,
                           'item_price': round(float(price_list.price) * 1.1, 2)}

    def test_create_success(self):
        response = SaleRecipe.create(self.data)

        self.assertIn('id', response.__dict__)
        price_list = self.data.get('recipe')

        self.assertEqual(response.profit, float(price_list.cost) * 2)
        self.assertEqual(response.profit_percentage, 50)

    def test_create_discount_success(self):
        response = SaleRecipe.create(self.discount_data)

        price = self.discount_data.get('recipe').price
        price = round(float(price), 2) * 2

        price_with_discount = round(price - (price * 0.2), 2)

        self.assertEqual(price_with_discount, response.price)

    def test_create_price_success(self):
        response = SaleRecipe.create(self.price_data)

        price = self.price_data.get('item_price')
        new_price = round(price, 2)

        self.assertEqual(new_price, response.item_price)
