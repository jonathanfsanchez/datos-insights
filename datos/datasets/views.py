from django.views import generic

from .models import Dataset


# Create your views here.
class DetailView(generic.DetailView):
    template_name = 'datasets/detail.html'
    model = Dataset


class IndexView(generic.ListView):
    template_name = 'datasets/index.html'
    model = Dataset
