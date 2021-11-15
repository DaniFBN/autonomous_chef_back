from django.test import TestCase
from model_bakery import baker

from apps.storage.classes.packaging_model import Packaging


class UpdatePackagingTestCase(TestCase):

    def setUp(self):
        baker.make('storage.Packaging', description='Desc')

        self.data = baker.prepare(
            'storage.Packaging',
            description='Desc').__dict__

    def test_update_success(self):
        old = Packaging.objects.get(id=1)

        new = Packaging.objects.get(id=1)
        new.update(self.data)

        self.assertEqual(old.id, new.id)
        self.assertNotEqual(old.name, new.name)
        self.assertNotEqual(old.amount, new.amount)
        self.assertNotEqual(old.price, new.price)

    def test_update_success_description(self):
        new = Packaging.objects.get(id=1)
        self.data.pop('description')
        new.update(self.data)

        self.assertEqual(new.description, None)
