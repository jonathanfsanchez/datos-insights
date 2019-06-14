from django.urls import path

from reviews.views import review_dataset_view, review_dataset_create, review_dataset_update, review_model_view, \
    review_model_create, review_model_update, review_model_delete

app_name = 'reviews'
urlpatterns = [
    path('dataset/<int:pk>/', review_dataset_view, name='review_dataset_view'),
    path('dataset/<int:pk>/new', review_dataset_create, name='review_dataset_create'),
    path('dataset/edit/<int:pk>', review_dataset_update, name='review_update'),

    path('model/<int:pk>/', review_model_view, name='review_model_view'),
    path('model/<int:pk>/new', review_model_create, name='review_model_create'),
    path('model/edit/<int:pk>', review_model_update, name='review_model_update'),

    path('model/delete/<int:pk>', review_model_delete, name='review_model_delete'),

]
