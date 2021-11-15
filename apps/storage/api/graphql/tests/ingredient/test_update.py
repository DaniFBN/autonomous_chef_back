from django.test import TestCase
from graphene.test import Client
from model_bakery import baker

from apps.storage.api.graphql.schema import schema


class ApiIngredientUpdateTestCase(TestCase):

    def setUp(self):
        baker.make('storage.Ingredient', description='Desc')

        self.client = Client(schema)
        self.query = '''
          mutation updateIngredient{
            updateIngredient(
              input: {
                id: 1
                name: "Update"
                amount: 3
                price: 20.01
              }
              
            ){
              name
              description
              amount
              price
            }
          }
        '''

        self.desc_query = '''
          mutation updateIngredient{
            updateIngredient(
              input: {
                id: 1
                name: "Update"
                description: "Update"
                amount: 2
                price: 2.32
              }
            ){
              name
              description
              amount
              price
            }
          }
        '''

    def test_update_success(self):
        response = self.client.execute(self.query)

        self.assertIn('data', response)
        self.assertIn('updateIngredient', response['data'])

        data = response['data']['updateIngredient']
        self.assertEqual(data['name'], 'Update')
        self.assertEqual(data['description'], None)
        self.assertEqual(data['amount'], 3)
        self.assertEqual(data['price'], 20.01)

    def test_update_description_success(self):
        response = self.client.execute(self.desc_query)

        data = response['data']['updateIngredient']
        self.assertEqual(data['description'], 'Update')
