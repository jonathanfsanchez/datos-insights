from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework.generics import CreateAPIView

from models.models import Model
from models.serializer import ModelApiCallSerializer
from users.models import DatosUser
from .models import DatasetSubscription, ModelSubscription, ModelApiCall


# Function that the CLIENT API should be calling.
# TODO: add user authentication?
# TODO: Add a function to create a session for the client api connection?
class ModelApiCallCreate(CreateAPIView):
    model = ModelApiCall
    serializer_class = ModelApiCallSerializer


class ModelSubForm(ModelForm):
    class Meta:
        model = ModelSubscription
        fields = []


@login_required
def subscription_list_view(request, template_name='subscriptions/subscription_list_view.html'):
    sort_by = request.GET.get('sortby')

    # if sort_by == 'all':
    # model = Model.objects.filter(modelsubscription__customer=request.user.id).distinct()
    # elif sort_by == 'inactive':
    model = Model.objects.filter(modelsubscription__customer=request.user.id).filter(
        modelsubscription__date_unsubscribed__isnull=True).distinct()
    # else:
    #     model = Model.objects.filter(modelsubscription__customer=request.user.id).filter(
    #         modelsubscription__date_unsubscribed__isnull=True).distinct()

    # dataset = DatasetSubscription.objects.filter(customer=request.user.id)

    context = dict()
    context['model_subs'] = model
    # context['dataset_subs'] = dataset

    return render(request=request, template_name=template_name, context=context)


# Create your views here.
def subscription_dataset_view(request, pk, template_name='subscriptions/subscription_dataset_view.html'):
    dataset_subscription = get_object_or_404(DatasetSubscription, pk=pk)
    return render(request=request, template_name=template_name, context={'dataset_subscription': dataset_subscription})


# def subscription_dataset_create(request, pk, template_name='reviews/subscription_dataset_form.html'):
#     form = DatasetReviewForm(request.POST or None)
#     if form.is_valid():
#         if request.user.is_authenticated:
#             form.instance.author = request.user
#             form.instance.dataset = Dataset.objects.get(pk=pk)
#             form.save()
#             return redirect('datasets:dataset_view', pk=pk)
#     return render(request, template_name, {'form': form})
#
#
# def subscription_dataset_update(request, pk, template_name='reviews/subscription_dataset_form.html'):
#     dataset = get_object_or_404(DatasetReview, pk=pk)
#     form = DatasetReviewForm(request.POST or None, instance=dataset)
#     if form.is_valid():
#         form.save()
#         return redirect('datasets:dataset_view', pk=pk)
#     return render(request, template_name, {'form': form})
@login_required
def subscription_model_list_view(request, pk, template_name='subscriptions/subscription_model_list_view.html'):
    """
    This view should show all the subscribers for a given model.

    """
    model = get_object_or_404(Model, pk=pk)

    page = request.GET.get('page')
    context = dict()

    subs = model.modelsubscription_set.filter(customer=request.user)

    if request.user == model.user:
        subs = model.modelsubscription_set.all()

    sub_page = Paginator(subs, 10)

    context['subs'] = sub_page.get_page(page)
    context['model'] = model

    return render(request=request, template_name=template_name, context=context)


# def subscription_model_view(request, pk, template_name='subscriptions/subscription_model_view.html'):
#     """
#     This view should show the details of one specific subscription. Not Required since we are abstracting subscriptions
#
#     """
#     model_subscription = get_object_or_404(ModelSubscription, pk=pk)
#     return render(request=request, template_name=template_name, context={'model_subscription': model_subscription})


@login_required
def subscription_model_create(request, pk):
    if request.POST:
        # check to see if there is an existing subscription for this model already
        if not Model.objects.get(pk=pk).modelsubscription_set.filter(
                customer=request.user.id).filter(date_unsubscribed__isnull=True).exists():
            subscription = ModelSubscription()
            subscription.customer = DatosUser.objects.get(pk=request.user.id)
            subscription.model = Model.objects.get(pk=pk)
            subscription.save()

        else:
            # already subscribed, skip - should be calling update to unsubscribe
            pass

    return redirect('models:model_view', pk=pk)


@login_required
def subscription_model_update(request, pk):
    if request.POST:
        if Model.objects.get(pk=pk).modelsubscription_set.filter(
                customer=request.user.id).filter(date_unsubscribed__isnull=True).exists():
            model_sub = ModelSubscription.objects.filter(model=pk).filter(customer=request.user.id).filter(
                date_unsubscribed__isnull=True)

            assert len(model_sub) == 1

            model_sub[0].date_unsubscribed = datetime.now(tz=timezone.utc)
            model_sub[0].save()

    return redirect('models:model_view', pk=pk)
#
#
# def subscription_model_update(request, pk, template_name='reviews/subscription_model_form.html'):
#     model_review = get_object_or_404(ModelReview, pk=pk)
#     form = ModelReviewForm(request.POST or None, instance=model_review)
#     if form.is_valid():
#         form.save()
#         return redirect('models:model_view', pk=pk)
#     return render(request, template_name, {'form': form})
