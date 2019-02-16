from django.contrib import admin

from .models import ModelReview, DatasetReview

# Register your models here.
admin.site.register(ModelReview)
admin.site.register(DatasetReview)
