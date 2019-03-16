from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Avg, Count

from datasets.models import Dataset


# Create your models here.
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

    def get_avg_stars(self):
        if self.modelreview_set.exists():
            return round(self.modelreview_set.aggregate(Avg('stars')).get('stars__avg') * 2) / 2
        else:
            return None

    def get_total_reviews(self):
        return self.modelreview_set.count()

    def get_total_api_calls(self):
        return self.modelsubscription_set.aggregate(Count('modelapicall')).get('modelapicall__count')

    def get_avg_api_calls(self):
        return self.modelsubscription_set.aggregate(Avg('modelapicall__process_time_ms')).get(
            'modelapicall__process_time_ms__avg')

    def get_total_api_calls_by_customer(self, pk):
        return self.modelsubscription_set.filter(customer=pk).aggregate(Count('modelapicall')).get(
            'modelapicall__count')

    def get_avg_api_calls_by_customer(self, pk):
        return self.modelsubscription_set.filter(customer=pk).aggregate(Avg('modelapicall__process_time_ms')).get(
            'modelapicall__process_time_ms__avg')

    def get_unique_subscribers(self):
        return self.modelsubscription_set.values('model__modelsubscription__customer').distinct().count()

    class Meta:
        db_table = 'models'


class ModelDatasetRelations(models.Model):
    model = models.ForeignKey(Model, models.DO_NOTHING, blank=False)
    dataset = models.ForeignKey('datasets.Dataset', models.DO_NOTHING, blank=False)
    date_related = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        db_table = "model_to_dataset"
        unique_together = ('model', 'dataset')
