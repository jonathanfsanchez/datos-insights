from django.db import models

# Create your models here.
from datos.datos import settings


class Dataset(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateField()
    is_private = models.BooleanField()
    cost = models.FloatField()
    dataset_path = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
