from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.db import models


class DatosUser(AbstractUser):

    model_bookmarks = models.ManyToManyField('models.Model')
    dataset_bookmarks = models.ManyToManyField('datasets.Dataset')
    # add additional fields in here
    pass
