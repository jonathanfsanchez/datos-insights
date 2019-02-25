from django.views import generic
from .models import Model


# Create your views here.
class DetailView(generic.DetailView):
    template_name = 'models/detail.html'
    model = Model


class IndexView(generic.ListView):
    template_name = 'models/index.html'
    model = Model
