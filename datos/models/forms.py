from django.forms import ModelForm

from models.models import Model


class DatosModelForm(ModelForm):
    class Meta:
        model = Model
        fields = ['title', 'description', 'is_private']
