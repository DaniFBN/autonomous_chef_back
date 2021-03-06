# Generated by Django 3.2.9 on 2021-11-13 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('unit_measurement', models.PositiveSmallIntegerField(choices=[(0, 'Gram'), (1, 'Milligram'), (2, 'Kilogram'), (3, 'Liter'), (4, 'Millilitem'), (5, 'Unity')], editable=False)),
                ('amount', models.SmallIntegerField(editable=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.AddConstraint(
            model_name='ingredient',
            constraint=models.CheckConstraint(check=models.Q(('unit_measurement__in', [0, 1, 2, 3, 4, 5])), name='ingredient_unit_measurement_valid'),
        ),
    ]
