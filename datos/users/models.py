from django.contrib.auth.models import AbstractUser


from django.db import models


class DatosUser(AbstractUser):

    # fields required for profile view
    # TODO: avatar field with image
    bio = models.TextField(blank=True)
    title = models.TextField(blank=True)
    company = models.TextField(blank=True)

    model_bookmarks = models.ManyToManyField('models.Model')
    dataset_bookmarks = models.ManyToManyField('datasets.Dataset')

    # for validating unique email addresses during auth
    class Meta(object):
        unique_together = ('email', )

    pass
