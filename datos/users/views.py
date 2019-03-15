from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

from .models import DatosUser


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def public_profile_view(request, pk):
    # todo
    return


@login_required
def private_profile_view(request):
    # todo
    return


def profile_view(request, pk, template_name="users/user_view.html"):
    datos_user = get_object_or_404(DatosUser, pk=pk)
    return render(request=request, template_name=template_name, context={'profile': datos_user})


@login_required
def uploads_view(request, template_name="users/my_uploads.html"):
    # datos_user = get_object_or_404(DatosUser, pk=pk)

    return render(request=request, template_name=template_name, context={})
