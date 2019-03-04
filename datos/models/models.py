from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from datasets.models import Dataset


class Model(models.Model):
    # ONNX = "O"
    # PYTORCH = "PY"
    # TENSORFLOW = "TF"
    #
    # FRAMEWORK_CHOICES = (
    #     (ONNX, 'ONNX'),
    #     (PYTORCH, 'Pytorch'),
    #     (TENSORFLOW, 'Tensorflow')
    # )

    title = models.TextField(blank=False)
    description = models.TextField(blank=True, default='')
    upload_date = models.DateTimeField(editable=False, auto_now_add=True)
    last_modified = models.DateTimeField(editable=False, auto_now=True)
    is_private = models.BooleanField(default=False)
    cost = models.FloatField(blank=False, default=0.00,
                             validators=[MinValueValidator(0.00), ])

    views = models.PositiveIntegerField(editable=False, default=0)
    # ml_framework = models.CharField(max_length=2, blank=False, choices=FRAMEWORK_CHOICES)

    weights_path = models.TextField()
    user = models.ForeignKey(get_user_model(), models.DO_NOTHING, blank=False)
    datasets = models.ManyToManyField(Dataset, through='ModelDatasetRelations')

    def __str__(self):
        return "{title} - {owner}".format(title=self.title, owner=self.user)

    class Meta:
        db_table = 'models'


class ModelDatasetRelations(models.Model):
    model = models.ForeignKey(Model, models.DO_NOTHING, blank=False)
    dataset = models.ForeignKey('datasets.Dataset', models.DO_NOTHING, blank=False)
    date_related = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        db_table = "model_to_dataset"
        unique_together = ('model', 'dataset')
