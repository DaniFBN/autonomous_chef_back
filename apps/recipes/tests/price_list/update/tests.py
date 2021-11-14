from django.test import TestCase
from model_bakery import baker
from apps.recipes.classes.price_list_model import PriceList


class UpdatePriceListTestCase(TestCase):

    def setUp(self):
        price_list = baker.make('recipes.PriceList', description='Desc')

        price = float(price_list.price) * 1.1
        self.data = {'price': round(price, 2)}
        self.desc_data = {**self.data, 'description': 'Desc'}

    def test_update_success(self):
        old = PriceList.objects.get(id=1)

        new = PriceList.objects.get(id=1)
        new.update(self.data)

        self.assertNotEqual(new.price, old.price)
        old_price = float(old.price)
        self.assertEqual(new.price, round(old_price * 1.1, 2))

    def test_update_description_success(self):
        old = PriceList.objects.get(id=1)

        new = PriceList.objects.get(id=1)
        new.update(self.desc_data)

        self.assertNotEqual(new.price, old.price)
        old_price = float(old.price)
        self.assertEqual(new.price, round(old_price * 1.1, 2))
