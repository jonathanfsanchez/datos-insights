from django.urls import path

from models.views import model_list, model_view, model_create, model_update, bookmark_model

app_name = 'models'
urlpatterns = [
    path('', model_list, name='model_list'),
    path('<int:pk>/', model_view, name='model_view'),
    path('new', model_create, name='model_create'),
    path('edit/<int:pk>', model_update, name='model_update'),
    path('<int:pk>/bookmark/', bookmark_model, name='bookmark_model'),
]