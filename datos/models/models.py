from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from datasets.models import Dataset


class Model(models.Model):
    title = models.TextField(blank=False)
    description = models.TextField(blank=True, default='')
    upload_date = models.DateTimeField(editable=False, auto_now_add=True)
    last_modified = models.DateTimeField(editable=False, auto_now=True)
    is_private = models.BooleanField(default=False)
    cost = models.FloatField(blank=False, default=0.00,
                             validators=[MinValueValidator(0.00), ])
    weights_path = models.TextField()
    user = models.ForeignKey(get_user_model(), models.DO_NOTHING, blank=False)
    datasets = models.ManyToManyField(Dataset, through='ModelDatasetRelations')

    class Meta:
        db_table = 'models'


class ModelDatasetRelations(models.Model):
    model = models.ForeignKey(Model, models.DO_NOTHING, blank=False)
    dataset = models.ForeignKey('datasets.Dataset', models.DO_NOTHING, blank=False)
    date_related = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        db_table = "model_to_dataset"
        unique_together = ('model', 'dataset')
