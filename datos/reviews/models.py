from django.db import models


# Create your models here.
from datos.datasets.models import Dataset
from datos.models.models import Model


class ModelReview(models.Model):
    review_text = models.TextField(blank=True, null=True)
    review_stars = models.IntegerField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    model = models.ForeignKey(Model, models.DO_NOTHING)
    model_review_category = models.ForeignKey('ModelReviewCategory', models.DO_NOTHING)


class ModelReviewCategory(models.Model):
    keyword = models.TextField(unique=True)


class DatasetReview(models.Model):
    review_text = models.TextField(blank=True, null=True)
    review_stars = models.IntegerField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING)
    dataset_review_category = models.ForeignKey('DatasetReviewCategory', models.DO_NOTHING)


class DatasetReviewCategory(models.Model):
    keyword = models.TextField(unique=True)
