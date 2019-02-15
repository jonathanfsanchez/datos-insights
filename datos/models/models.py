from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Model(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=False)
    cost = models.FloatField()
    weights_path = models.TextField()
    user = models.ForeignKey(get_user_model(), models.DO_NOTHING)

    class Meta:
        db_table = 'models'


class ModelDatasetRelations(models.Model):
    model = models.ForeignKey(Model, models.DO_NOTHING)
    dataset = models.ForeignKey('datasets.Dataset', models.DO_NOTHING)

    class Meta:
        db_table = "model_to_dataset"
        unique_together = ('model', 'dataset')
