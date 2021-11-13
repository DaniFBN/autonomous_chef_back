from django.db import models

from apps.storage.utils.enums.unit_measurement import UnitMeasurement

_CONSTRAINTS = {
    'name': 'ingredient_unit_measurement_valid',
    'check': models.Q(unit_measurement__in=UnitMeasurement.valid_values())
}


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, null=True)
    unit_measurement = models.PositiveSmallIntegerField(
        choices=UnitMeasurement.choices(),
        editable=False
    )
    amount = models.SmallIntegerField(editable=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        constraints = (models.CheckConstraint(**_CONSTRAINTS),)

    @classmethod
    def create(cls, data):
        obj = cls()
        obj.name = data.get('name')
        obj.unit_measurement = data.get('unit_measurement')
        obj.amount = data.get('amount')
        obj.price = data.get('price')

        if 'description' in data:
            obj.description = data.get('description')

        obj.save()

        return obj

    def update(self, data):
        self.name = data.get('name')
        self.amount = data.get('amount')
        self.price = data.get('price')

        if 'description' in data:
            self.description = data.get('description')

        self.save()

        return self
