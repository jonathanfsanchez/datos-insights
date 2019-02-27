from django.shortcuts import render, get_object_or_404

from .models import DatasetSubscription, ModelSubscription


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


def subscription_model_view(request, pk, template_name='subscriptions/subscription_model_view.html'):
    model_subscription = get_object_or_404(ModelSubscription, pk=pk)
    return render(request=request, template_name=template_name, context={'model_subscription': model_subscription})

# def subscription_model_create(request, pk, template_name='reviews/subscription_model_form.html'):
#     form = ModelReviewForm(request.POST or None)
#     if form.is_valid():
#         if request.user.is_authenticated:
#             form.instance.author = request.user
#             form.instance.dataset.id = Model.objects.get(pk=pk)
#             form.save()
#             return redirect('models:model_view', pk=pk)
#     return render(request, template_name, {'form': form})
#
#
# def subscription_model_update(request, pk, template_name='reviews/subscription_model_form.html'):
#     model_review = get_object_or_404(ModelReview, pk=pk)
#     form = ModelReviewForm(request.POST or None, instance=model_review)
#     if form.is_valid():
#         form.save()
#         return redirect('models:model_view', pk=pk)
#     return render(request, template_name, {'form': form})
