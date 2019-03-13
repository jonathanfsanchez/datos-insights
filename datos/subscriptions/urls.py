from django.urls import path

from subscriptions.views import subscription_dataset_view, subscription_model_view, subscription_model_create, \
    subscription_model_update, subscription_list_view, subscription_model_list_view

app_name = 'subscriptions'

urlpatterns = [
    # subscriptions linked to the logged in user
    path('', subscription_list_view, name='subscription_list_view'),

    path('dataset/detail/<int:pk>/', subscription_dataset_view, name='subscription_dataset_view'),
    # path('dataset/<int:pk>/new', subscription_dataset_create, name='subscription_dataset_create'),
    # path('dataset/edit/<int:pk>', subscription_dataset_update, name='subscription_update'),

    path('model/<int:pk>', subscription_model_list_view, name='subscription_model_list_view'),

    # the details of an atomic subscription
    path('model/detail/<int:pk>/', subscription_model_view, name='subscription_model_view'),
    # subscribe button
    path('model/<int:pk>/new', subscription_model_create, name='subscription_model_create'),
    # unsubscribe button
    path('model/edit/<int:pk>', subscription_model_update, name='subscription_model_update'),
]
