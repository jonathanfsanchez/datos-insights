from django.contrib.auth import get_user_model
from django.db import models


class ModelApiCall(models.Model):
    inference_date_start = models.DateTimeField(editable=False, auto_now_add=True)
    process_time_ms = models.FloatField(blank=False)
    model_subscription = models.ForeignKey('subscriptions.ModelSubscription', models.DO_NOTHING, blank=False)

    # cold start - keep track of api calls that are required re-deployment(?)

    class Meta:
        db_table = 'model_api_calls'


class DatasetApiCall(models.Model):
    download_date_start = models.DateTimeField(editable=False, auto_now_add=True)
    dataset_subscription = models.ForeignKey('subscriptions.DatasetSubscription', models.DO_NOTHING, blank=False)

    class Meta:
        db_table = 'dataset_api_calls'


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
    # expiration = models.DateField(blank=True, null=True, default=None)
    date_subscribed = models.DateTimeField(editable=False, auto_now_add=True)
    date_unsubscribed = models.DateTimeField(null=True, default=None)
    customer = models.ForeignKey(get_user_model(), models.DO_NOTHING, blank=False)
    model = models.ForeignKey('models.Model', models.DO_NOTHING, blank=False)

    def api_calls(self):
        return self.modelapicall_set.count()

    def is_active(self):
        return self.date_unsubscribed is None

    def __str__(self):
        return "{} - {}".format(self.customer, self.model.title)

    class Meta:
        db_table = 'model_subscriptions'
        ordering = ['-date_subscribed']


class DatasetSubscription(models.Model):
    ONE_TIME = 1
    UNLIMITED = 2

    SUBSCRIPTION_CHOICES = (
        (ONE_TIME, 'One Time Download'),
        (UNLIMITED, 'Unlimited Downloads')
    )

    subscription_type = models.IntegerField(choices=SUBSCRIPTION_CHOICES, default=UNLIMITED)

    # expiration = models.DateField(blank=True, null=True, default=None)
    date_subscribed = models.DateTimeField(editable=False, auto_now_add=True)
    date_unsubscribed = models.DateTimeField(default=None)
    customer = models.ForeignKey(get_user_model(), models.DO_NOTHING, blank=False)
    dataset = models.ForeignKey('datasets.Dataset', models.DO_NOTHING, blank=False)

    class Meta:
        db_table = 'dataset_subscriptions'
        ordering = ['-date_subscribed']
