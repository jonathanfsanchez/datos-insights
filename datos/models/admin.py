from django.contrib import admin

from .models import ModelDatasetRelations, Model

# Register your models here.
admin.site.register(Model)
admin.site.register(ModelDatasetRelations)
