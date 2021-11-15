from django.test import TestCase
from graphene.test import Client
from model_bakery import baker

from apps.storage.api.graphql.schema import schema
from apps.utils.helpers_gql_tests import GqlDeleteNotFoundTestMixin


class ApiIngredientDeleteTestCase(TestCase, GqlDeleteNotFoundTestMixin):

    def setUp(self):
        baker.make('storage.Ingredient')

        self.client = Client(schema)
        self.query = '''
          mutation deleteIngredient{
            deleteIngredient(  
              id: 1
            ){
              ok
            }
          }
        '''
        
        # GqlDeleteNotFoundTestMixin dependencies
        self.mutation = 'deleteIngredient'
        self.not_found_query = '''
          mutation deleteIngredient{
            deleteIngredient(  
              id: 2
            ){
              ok
            }
          }
        '''

    def test_delete_success(self):
        response = self.client.execute(self.query)

        self.assertIn('data', response)
        self.assertIn('deleteIngredient', response['data'])

        data = response['data']['deleteIngredient']
        self.assertEqual(data['ok'], True)
