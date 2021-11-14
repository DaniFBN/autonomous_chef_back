from django.db import models

from apps.storage.classes.packaging_model import Packaging


# Allows a Recipe to have a set of packaging
class RecipePackaging(models.Model):
    packaging = models.ManyToManyField(Packaging)

    @classmethod
    def create(cls, data):
        ''' data = { packaging: Packaging[]} '''
        obj = cls()
        obj.save()

        packaging = data.get('packaging')
        obj.__add_packaging(packaging)

        return obj

    def update(self, data):
        ''' data = { packaging: Packaging[]} '''

        packaging = data.get('packaging')
        self.__handle_remove_packaging(packaging)
        self.__handle_add_packaging(packaging)

    @property
    def price(self):
        ''' Sum the unit cost of all packaging '''
        final_price = 0.0

        for pack in self.__all_packaging():
            final_price += pack.unit_cost

        return round(final_price, 2)

    def __handle_add_packaging(self, packaging):
        ''' Compare Set and List, get Packaging to add, and add'''
        packaging = set(packaging)

        add_packaging = packaging.difference(self.__all_packaging())

        self.__add_packaging(list(add_packaging))

    def __handle_remove_packaging(self, packaging):
        ''' Compare Set and List, get Packaging to remove, and remove'''
        current = set(self.__all_packaging())

        remove_packaging = current.difference(packaging)

        self.__remove_packaging(list(remove_packaging))

    def __all_packaging(self):
        return self.packaging.all()

    def __add_packaging(self, values):
        ''' 
        Only add Packaging. 
        values = Packaging[] 
        '''

        for value in values:
            self.packaging.add(value)

    def __remove_packaging(self, values):
        ''' 
        Only remove Packaging. 
        values = Packaging[] 
        '''

        for value in values:
            self.packaging.remove(value)
