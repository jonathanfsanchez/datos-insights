from django.contrib import admin

from .models import ModelSubscription, DatasetSubscription

# Register your models here.
admin.site.register(ModelSubscription)
admin.site.register(DatasetSubscription)
