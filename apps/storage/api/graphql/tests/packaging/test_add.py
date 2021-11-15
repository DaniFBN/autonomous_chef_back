from django.test import TestCase
from graphene.test import Client
from model_bakery import baker

from apps.storage.api.graphql.schema import schema


class ApiPackagingAddTestCase(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.query = '''
          mutation addPackaging{
            addPackaging(
              input: {
                name: "Name"
                description: "Desc"
                unitMeasurement: 1
                amount: 2
                price: 2.32
              }
            ){
              name
              description
              unitMeasurement
              amount
              price
            }
          }
        '''

        self.desc_query = '''
          mutation addPackaging{
            addPackaging(
              input: {
                name: "Name"
                unitMeasurement: 1
                amount: 2
                price: 2.32
              }
            ){
              name
              description
              unitMeasurement
              amount
              price
            }
          }
        '''

    def test_add_success(self):
        response = self.client.execute(self.query)

        self.assertIn('data', response)
        self.assertIn('addPackaging', response['data'])

        data = response['data']['addPackaging']
        self.assertEqual(data['name'], 'Name')
        self.assertEqual(data['description'], 'Desc')
        self.assertEqual(data['unitMeasurement'], 1)
        self.assertEqual(data['amount'], 2)
        self.assertEqual(data['price'], 2.32)

    def test_add_description_success(self):
        response = self.client.execute(self.desc_query)

        data = response['data']['addPackaging']
        self.assertEqual(data['description'], None)
