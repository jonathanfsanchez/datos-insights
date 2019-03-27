from django.urls import path

from .views import profile_view, SignUp, uploads_view, bookmarks_view

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/<int:pk>', profile_view, name='profile_view'),
    path('uploads/', uploads_view, name='uploads_view'),
    path('bookmarks/', bookmarks_view, name='bookmarks_view'),
]
