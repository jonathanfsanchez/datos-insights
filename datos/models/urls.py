from django.urls import path

from .views import DetailView, IndexView

app_name = 'models'
urlpatterns = [
    # ex /models/
    path('', IndexView.as_view(), name='index'),
    # ex: /models/7
    path('<int:pk>/', DetailView.as_view(), name='detail'),
]