from django.db import models


# Create your models here.
from datos.datasets.models import Dataset
from datos.datos import settings


class Model(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=False)
    cost = models.FloatField()
    weights_path = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)


class ModelDatasetRelations(models.Model):
    model = models.ForeignKey(Model, models.DO_NOTHING)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING)

    class Meta:
        unique_together = ('model', 'dataset')
