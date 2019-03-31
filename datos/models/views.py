from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from models.forms import DatosModelForm
from models.models import Model
from users.models import DatosUser


# Create your views here.
def model_list(request, template_name='models/model_list.html'):
    # TODO find a way to do featured/popular models
    featured = Model.objects.all()[0:3]
    popular = Model.objects.all()[3:6]
    context = dict()
    context['featured'] = featured
    context['popular'] = popular

    return render(request, template_name, context=context)


def model_view(request, pk, template_name='models/model_view.html'):
    model = get_object_or_404(Model, pk=pk)

    context = dict()
    context['model'] = model

    if request.user.is_authenticated:

        if request.user.id == model.user.id:
            # all users api calls
            context['api_calls'] = model.get_total_api_calls()
            context['api_calls_avg'] = model.get_avg_api_calls()
        else:
            context['api_calls'] = model.get_total_api_calls_by_customer(request.user.id)
            context['api_calls_avg'] = model.get_avg_api_calls_by_customer(request.user.id)

    return render(request, template_name, context=context)


@login_required
def model_create(request, template_name='models/model_form.html'):
    form = DatosModelForm(request.POST or None)
    if form.is_valid():
        new_model = form.save()
        return redirect('models:model_view', pk=new_model.pk)
    return render(request, template_name, {'form': form})

@login_required
def model_update(request, pk, template_name='models/model_form.html'):
    dataset = get_object_or_404(Model, pk=pk)
    form = DatosModelForm(request.POST or None, instance=dataset)
    if form.is_valid():
        new_model = form.save()
        return redirect('models:model_view', pk=new_model.pk)
    return render(request, template_name, {'form': form})


@login_required
def bookmark_model(request, pk):
    if request.POST:
        model = Model.objects.get(pk=pk)
        if model.datosuser_set.filter(pk=request.user.id).exists():
            model.datosuser_set.remove(DatosUser.objects.get(pk=request.user.id))
        else:
            model.datosuser_set.add(DatosUser.objects.get(pk=request.user.id))

    return redirect('models:model_view', pk=pk)
