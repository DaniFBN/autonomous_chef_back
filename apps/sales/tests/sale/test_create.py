from django.test import TestCase
from model_bakery import baker

from apps.sales.classes.sale_model import Sale


class CreateSaleTestCase(TestCase):

    def setUp(self):
        recipes = []
        all_cost = 0.0
        all_price = 0.0
        for i in range(0, 3):
            packaging = baker.make('recipes.RecipePackaging', make_m2m=True)
            recipe = baker.make('recipes.Recipe', packaging=packaging)

            price = round(float(recipe.cost) * 2, 2)
            price_list = baker.make('recipes.PriceList', recipe=recipe,
                                    price=price)

            all_cost += float(recipe.cost)
            all_price += price

            sale = baker.make('sales.SaleRecipe', recipe=price_list, amount=1,
                              item_price=price, item_cost=recipe.cost)

            recipes.append(sale)

        self.all_cost = round(all_cost, 2)
        self.all_price = round(all_price, 2)
        self.data = {'recipes': recipes}

    def test_create_success(self):
        response = Sale.create(self.data)

        self.assertIn('id', response.__dict__)
        self.assertIn('date', response.__dict__)

        for recipe in self.data.get('recipes'):
            self.assertIn(recipe, response.recipes.all())

        self.assertEqual(response.price, self.all_price)

        profit = self.all_price - self.all_cost
        self.assertEqual(profit, response.profit)
