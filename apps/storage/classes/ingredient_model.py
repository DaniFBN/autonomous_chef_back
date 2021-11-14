from django.core.validators import MinValueValidator
from django.db import models

from apps.storage.utils.enums.unit_measurement import UnitMeasurement

_CONSTRAINTS = {
    'name': 'ingredient_unit_measurement_valid',
    'check': models.Q(unit_measurement__in=UnitMeasurement.valid_values())
}


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, null=True)

    # Saved for better future understanding
    unit_measurement = models.PositiveSmallIntegerField(
        choices=UnitMeasurement.choices(),
        editable=False
    )
    # Used to specific values of weight or volume
    amount = models.PositiveSmallIntegerField(editable=False)

    # Cost price - Max value is 9999.99
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[
                                MinValueValidator('0.01')])

    class Meta:
        constraints = (models.CheckConstraint(**_CONSTRAINTS),)

    @classmethod
    def create(cls, data):
        ''' data = { name, unit_measurement, amount, price, description? } '''
        obj = cls(**data)
        obj.save()

        return obj

    def update(self, data):
        ''' data = { name, amount, price, description? } '''

        self.name = data.get('name')
        self.amount = data.get('amount')
        self.price = data.get('price')

        # Change description if has in data,
        # or dont have in data and obj has description, change to None
        if 'description' in data:
            self.description = data.get('description')
        elif self.description:
            self.description = None

        self.save()

        return self
