from django.urls import path

from subscriptions.views import subscription_dataset_view, subscription_model_view, subscription_model_create, \
    subscription_model_update

app_name = 'subscriptions'

urlpatterns = [
    path('dataset/<int:pk>/', subscription_dataset_view, name='subscription_dataset_view'),
    # path('dataset/<int:pk>/new', subscription_dataset_create, name='subscription_dataset_create'),
    # path('dataset/edit/<int:pk>', subscription_dataset_update, name='subscription_update'),

    path('model/<int:pk>/', subscription_model_view, name='subscription_model_view'),
    path('model/<int:pk>/new', subscription_model_create, name='subscription_model_create'),
    path('model/edit/<int:pk>', subscription_model_update, name='subscription_model_update'),
]
