from django.forms import ModelForm

from reviews.models import DatasetReview, ModelReview


class DatasetReviewForm(ModelForm):
    class Meta:
        model = DatasetReview
        fields = ['title', 'text', 'stars']


class ModelReviewForm(ModelForm):
    class Meta:
        model = ModelReview
        fields = ['title', 'text', 'stars']