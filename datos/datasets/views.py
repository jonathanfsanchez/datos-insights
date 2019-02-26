from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect

from .models import Dataset


# Create your views here.
class DatasetForm(ModelForm):
    class Meta:
        model = Dataset
        fields = ['title', 'description', 'is_private']


def dataset_list(request, template_name='datasets/dataset_list.html'):
    dataset = Dataset.objects.all()
    return render(request, template_name, {'object_list': dataset})


def dataset_view(request, pk, template_name='datasets/dataset_view.html'):
    dataset = get_object_or_404(Dataset, pk=pk)
    return render(request, template_name, {'dataset': dataset})


def dataset_create(request, template_name='datasets/dataset_form.html'):
    form = DatasetForm(request.POST or None)
    if form.is_valid():
        new_ds = form.save()
        return redirect('datasets:dataset_view', pk=new_ds.pk)
    return render(request, template_name, {'form': form})


def dataset_update(request, pk, template_name='datasets/dataset_form.html'):
    dataset = get_object_or_404(Dataset, pk=pk)
    form = DatasetForm(request.POST or None, instance=dataset)
    if form.is_valid():
        new_ds = form.save()
        return redirect('datasets:dataset_view', pk=new_ds.pk)
    return render(request, template_name, {'form': form})

# def dataset_delete(request, pk, template_name='datasets/dataset_confirm_delete.html'):
#     dataset = get_object_or_404(Dataset, pk=pk)
#     if request.method == 'POST':
#         dataset.delete()
#         return redirect('dataset_list')
#     return render(request, template_name, {'object': dataset})
