# Generated by Django 3.2.9 on 2021-11-14 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20211113_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='packaging',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipepackaging'),
        ),
    ]
