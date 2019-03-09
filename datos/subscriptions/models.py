from django.contrib.auth import get_user_model
from django.db import models


class ModelApiCalls(models.Model):
    inference_date_start = models.DateTimeField(editable=False, auto_now_add=True)
    process_time_ms = models.FloatField(blank=False)
    subscription = models.ForeignKey('subscriptions.ModelSubscription', models.DO_NOTHING, blank=False)
    # cold start - keep track of api calls that are required re-deployment(?)

    class Meta:
        db_table = 'model_api_calls'


# Create your models here.
class ModelSubscription(models.Model):
    PER_INFERENCE = "PI"
    # PER_YEAR = "PY" # Not in scope of MVP
    # PER_MONTH = "PM" # Not in scope of MVP

    SUBSCRIPTION_CHOICES = (
        (PER_INFERENCE, 'Per Inference'),
        # (PER_YEAR, 'Per Year'), # Not in scope of MVP
        # (PER_MONTH, 'Per Month') # Not in scope of MVP
    )

    subscription_type = models.CharField(max_length=2, choices=SUBSCRIPTION_CHOICES, default=PER_INFERENCE)

    is_active = models.BooleanField(default=True)
    url = models.TextField()
    expiration = models.DateField(blank=True, null=True, default=None)
    date_subscribed = models.DateTimeField(editable=False, auto_now_add=True)
    customer = models.ForeignKey(get_user_model(), models.DO_NOTHING, blank=False)
    model = models.ForeignKey('models.Model', models.DO_NOTHING, blank=False)

    class Meta:
        db_table = 'model_subscriptions'
        unique_together = ('customer', 'model')
        ordering = ['date_subscribed']


class DatasetSubscription(models.Model):
    ONE_TIME = 1
    UNLIMITED = 2

    SUBSCRIPTION_CHOICES = (
        (ONE_TIME, 'One Time Download'),
        (UNLIMITED, 'Unlimited Downloads')
    )

    subscription_type = models.IntegerField(choices=SUBSCRIPTION_CHOICES, default=UNLIMITED)

    is_active = models.BooleanField(default=True)
    url = models.TextField()
    expiration = models.DateField(blank=True, null=True, default=None)
    date_subscribed = models.DateTimeField(editable=False, auto_now_add=True)
    customer = models.ForeignKey(get_user_model(), models.DO_NOTHING, blank=False)
    dataset = models.ForeignKey('datasets.Dataset', models.DO_NOTHING, blank=False)

    class Meta:
        db_table = 'dataset_subscriptions'
        unique_together = ('customer', 'dataset')
        ordering = ['date_subscribed']
