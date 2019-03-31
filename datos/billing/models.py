from django.db import models

# Create your models here.
from subscriptions.models import ModelApiCall


class ModelBillCycle(models.Model):
    cycle_start = models.DateTimeField(editable=False, auto_now_add=True, blank=False)
    cycle_end = models.DateTimeField(editable=False, blank=False)

    def __str__(self):
        return str(self.cycle_start) + " - " + str(self.cycle_end)


class ModelBill(models.Model):
    bill_cycle = models.ForeignKey(ModelBillCycle, models.DO_NOTHING, blank=False)
    model_api_call_start = models.ForeignKey(ModelApiCall, models.DO_NOTHING, blank=False)
    model_api_call_start = models.ForeignKey(ModelApiCall, models.DO_NOTHING, blank=False)

    def __str__(self):
        return self.model_api_call_start.model_subscription.customer + ": " + str(self.bill_cycle)
