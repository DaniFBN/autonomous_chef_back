from django.db import models

from apps.storage.classes.packaging_model import Packaging


class RecipePackaging(models.Model):
    packaging = models.ManyToManyField(Packaging)