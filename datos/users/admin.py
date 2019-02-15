from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import DatosUser

# Register your models here.
admin.site.register(DatosUser, UserAdmin)
