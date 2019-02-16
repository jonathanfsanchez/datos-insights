from django.urls import path

from .views import DetailView, IndexView

app_name = 'datasets'
urlpatterns = [
    # ex /datasets/
    path('', IndexView.as_view(), name='index'),
    # ex: /datasets/5/
    path('<int:pk>/', DetailView.as_view(), name='detail'),
]