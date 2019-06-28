# used for overwriting django user creation
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DatosUser

class DatosUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = DatosUser
        fields = ('username',)
