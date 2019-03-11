from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect

from models.models import Model
from users.models import DatosUser


# Create your views here.
class DatosModelForm(ModelForm):
    class Meta:
        model = Model
        fields = ['title', 'description', 'is_private']


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
    related = Model.objects.all()[0:3]

    reviews = model.modelreview_set.all()
    review_page = Paginator(reviews, 5)

    subscribers = model.modelsubscription_set.all()
    subscribe_page = Paginator(subscribers, 1)

    page = request.GET.get('page')
    sub_page = request.GET.get('sub_page')

    context = dict()
    context['model'] = model
    context['related'] = related

    context['reviews'] = review_page.get_page(page)
    context['subscribers'] = subscribe_page.get_page(sub_page)

    context['render_subscribers'] = request.user.id == model.user.id

    context['bookmark_to_render'] = None

    if request.user.is_authenticated:
        if model.datosuser_set.filter(pk=request.user.id).exists():
            # is bookmarked
            context['bookmark_to_render'] = 'bookmark'
        else:
            context['bookmark_to_render'] = 'bookmark_border'

    return render(request, template_name, context=context)


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


@login_required
def bookmark_model(request, pk):
    model = Model.objects.get(pk=pk)
    if model.datosuser_set.filter(pk=request.user.id).exists():
        model.datosuser_set.remove(DatosUser.objects.get(pk=request.user.id))
    else:
        model.datosuser_set.add(DatosUser.objects.get(pk=request.user.id))

    return redirect('models:model_view', pk=pk)
