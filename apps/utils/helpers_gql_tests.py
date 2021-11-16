class GqlDeleteNotFoundTestMixin():

    def test_delete_not_found(self):
        response = self.client.execute(self.not_found_query)

        self.assertIn('data', response)
        self.assertIn(self.mutation, response['data'])
        data = response['data'][self.mutation]

        self.assertEqual(data, None)

        self.assertIn('errors', response)
