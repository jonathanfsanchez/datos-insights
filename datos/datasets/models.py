from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from django.urls import reverse


# Create your models here.
class Dataset(models.Model):
    title = models.TextField(blank=False)
    description = models.TextField(blank=True, default='')
    upload_date = models.DateTimeField(editable=False, auto_now_add=True)
    last_modified = models.DateTimeField(editable=False, auto_now=True)
    is_private = models.BooleanField(default=False)
    cost = models.FloatField(blank=False, default=0.00,
                             validators=[MinValueValidator(0.00), ])
    dataset_path = models.TextField()
    user = models.ForeignKey(get_user_model(), models.DO_NOTHING, blank=False)

    def __str__(self):
        return "{title} - {owner}".format(title=self.title, owner=self.user)

    def get_absolute_url(self):
        return reverse('dataset_edit', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'datasets'
