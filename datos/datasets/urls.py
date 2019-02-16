from django.urls import path

from . import views

app_name = 'datasets'
urlpatterns = [
    # ex: /datasets/5/
    path('<int:pk>/', views.DetailView.as_view(template_name='datasets/detail.html'), name='detail'),
]