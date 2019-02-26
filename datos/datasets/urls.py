from django.urls import path

from datasets.views import dataset_list, dataset_update, dataset_create, dataset_view

app_name = 'datasets'
urlpatterns = [
    path('', dataset_list, name='dataset_list'),
    path('<int:pk>/', dataset_view, name='dataset_view'),
    path('new', dataset_create, name='dataset_create'),
    path('edit/<int:pk>', dataset_update, name='dataset_update'),
]