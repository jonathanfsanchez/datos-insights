from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class ModelReview(models.Model):
    title = models.TextField(blank=False)
    text = models.TextField(blank=True, default="")
    stars = models.IntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    original_date = models.DateTimeField(editable=False, auto_now_add=True)
    last_modified = models.DateTimeField(editable=False, auto_now=True)

    author = models.ForeignKey(get_user_model(), models.DO_NOTHING, blank=False)
    model = models.ForeignKey('models.Model', models.DO_NOTHING)

    # model_review_category = models.ForeignKey('ModelReviewCategory', models.DO_NOTHING)

    class Meta:
        db_table = 'model_reviews'
        unique_together = ('author', 'model')


class DatasetReview(models.Model):
    title = models.TextField(blank=False)
    text = models.TextField(blank=True, default="")
    stars = models.IntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    original_date = models.DateTimeField(editable=False, auto_now_add=True)
    last_modified = models.DateTimeField(editable=False, auto_now=True)

    author = models.ForeignKey(get_user_model(), models.DO_NOTHING, blank=False)
    dataset = models.ForeignKey('datasets.Dataset', models.DO_NOTHING)

    # dataset_review_category = models.ForeignKey('DatasetReviewCategory', models.DO_NOTHING)

    class Meta:
        db_table = 'dataset_reviews'
        unique_together = ('author', 'dataset')


#TODO review of services, e.g data collection review, data labeling review, training new model, data analysis
# class ServiceReview(models.Model):
#     title = models.TextField(blank=False)
#     text = models.TextField(blank=True, default="")
#     stars = models.IntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
#     original_date = models.DateTimeField(editable=False, auto_now_add=True)
#     last_modified = models.DateTimeField(editable=False, auto_now=True)
#
#     author = models.ForeignKey(get_user_model(), models.DO_NOTHING, blank=False)
#     service_provider = models.ForeignKey(get_user_model(), models.DO_NOTHING(), blank=False)
#
#     class Meta:
#         db_table = 'dataset_reviews'
#         unique_together = ('author', 'service_provider')


# class ModelReviewCategory(models.Model):
#     keyword = models.TextField(unique=True)


# class DatasetReviewCategory(models.Model):
#     keyword = models.TextField(unique=True)
