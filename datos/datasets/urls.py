from django.urls import path

from .views import dataset_create, dataset_view, dataset_list, dataset_update

app_name = 'datasets'
urlpatterns = [
    path('', dataset_list, name='dataset_list'),
    path('<int:pk>/', dataset_view, name='dataset_view'),
    path('new', dataset_create, name='dataset_new'),
    path('edit/<int:pk>', dataset_update, name='dataset_edit'),
]