from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import DatosUserCreationForm, DatosUserChangeForm
from .models import DatosUser


# custom user admin creation for profile views
class CustomUserAdmin(UserAdmin):
    add_form = DatosUserCreationForm
    form = DatosUserChangeForm
    model = DatosUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio',
                           'title',
                           'company', )}), )

admin.site.register(DatosUser, CustomUserAdmin)
