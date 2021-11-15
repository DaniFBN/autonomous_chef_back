from django.test import TestCase
from graphene.test import Client
from model_bakery import baker

from apps.storage.api.graphql.schema import schema
from apps.utils.helpers_tests_graphql import GqlDeleteNotFoundTestMixin


class ApiPackagingDeleteTestCase(TestCase, GqlDeleteNotFoundTestMixin):

    def setUp(self):
        baker.make('storage.Packaging')

        self.client = Client(schema)
        self.query = '''
          mutation deletePackaging{
            deletePackaging(  
              id: 1
            ){
              ok
            }
          }
        '''
        
        # GqlDeleteNotFoundTestMixin dependencies
        self.mutation = 'deletePackaging'
        self.not_found_query = '''
          mutation deletePackaging{
            deletePackaging(  
              id: 2
            ){
              ok
            }
          }
        '''

    def test_delete_success(self):
        response = self.client.execute(self.query)

        self.assertIn('data', response)
        self.assertIn('deletePackaging', response['data'])

        data = response['data']['deletePackaging']
        self.assertEqual(data['ok'], True)
