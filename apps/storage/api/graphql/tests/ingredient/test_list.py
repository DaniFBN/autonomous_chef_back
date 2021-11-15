from django.test import TestCase
from graphene.test import Client
from model_bakery import baker

from apps.storage.api.graphql.schema import schema


class ApiIngredientListTestCase(TestCase):

    def setUp(self):
        baker.make('storage.Ingredient')
      
        self.client = Client(schema)
        self.query = '''
          query allIngredients{
            allIngredients{
              id
              name
              description
              unitMeasurement
              amount
              price
            }
          }
        '''

    def test_list_all(self):
        response = self.client.execute(self.query)

        self.assertIn('data', response)
        self.assertIn('allIngredients', response['data'])
        self.assertIsInstance(response['data']['allIngredients'], list)
        self.assertEqual(len(response['data']['allIngredients']), 1)