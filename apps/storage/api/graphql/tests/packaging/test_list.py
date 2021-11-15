from django.test import TestCase
from graphene.test import Client
from model_bakery import baker

from apps.storage.api.graphql.schema import schema


class ApiPackagingListTestCase(TestCase):

    def setUp(self):
        baker.make('storage.Packaging')
      
        self.client = Client(schema)
        self.query = '''
          query allPackaging{
            allPackaging{
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
        self.assertIn('allPackaging', response['data'])
        self.assertIsInstance(response['data']['allPackaging'], list)
        self.assertEqual(len(response['data']['allPackaging']), 1)