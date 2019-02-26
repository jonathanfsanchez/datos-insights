from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect

from models.models import Model


# Create your views here.
class DatosModelForm(ModelForm):
    class Meta:
        model = Model
        fields = ['title', 'description', 'is_private']


def model_list(request, template_name='models/model_list.html'):
    model = Model.objects.all()
    return render(request, template_name, {'object_list': model})


def model_view(request, pk, template_name='models/model_view.html'):
    model = get_object_or_404(Model, pk=pk)
    return render(request, template_name, {'model': model})


def model_create(request, template_name='models/model_form.html'):
    form = DatosModelForm(request.POST or None)
    if form.is_valid():
        new_model = form.save()
        return redirect('models:model_view', pk=new_model.pk)
    return render(request, template_name, {'form': form})


def model_update(request, pk, template_name='models/model_form.html'):
    dataset = get_object_or_404(Model, pk=pk)
    form = DatosModelForm(request.POST or None, instance=dataset)
    if form.is_valid():
        new_model = form.save()
        return redirect('models:model_view', pk=new_model.pk)
    return render(request, template_name, {'form': form})
