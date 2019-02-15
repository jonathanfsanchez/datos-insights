from django.db import models


# Create your models here.
class ModelSubscription(models.Model):
    is_active = models.BooleanField()
    url = models.TextField()
    expiration = models.DateField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    model = models.ForeignKey(Model, models.DO_NOTHING)


class DatasetSubscription(models.Model):
    is_active = models.BooleanField()
    url = models.TextField()
    expiration = models.DateField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING)
