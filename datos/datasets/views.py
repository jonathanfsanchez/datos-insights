from django.shortcuts import render
from django.views import generic

from .models import Dataset


# Create your views here.
class DetailView(generic.DetailView):
    model = Dataset
