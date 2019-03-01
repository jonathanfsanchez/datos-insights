from django.urls import path

from .views import profile_view, SignUp

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/<int:pk>', profile_view, name='profile_view'),
]
