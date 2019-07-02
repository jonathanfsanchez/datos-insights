# used for overwriting django user creation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import DatosUser


class DatosUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = DatosUser
        fields = ('username', 'email', )


class DatosUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = DatosUser
        fields = ('first_name', 'last_name', 'email', 'bio', 'title', 'company', )
