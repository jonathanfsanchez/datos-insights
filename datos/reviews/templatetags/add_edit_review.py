from django import template

from models.models import Model
from users.models import DatosUser

register = template.Library()


@register.inclusion_tag('reviews/_add_edit_button.html', takes_context=True)
def add_edit_btn(context, user: DatosUser, model: Model):
    if user == model.user or not user.is_authenticated:
        return

    # edit the review
    elif user.modelreview_set.filter(model=model).exists():
        review = user.modelreview_set.filter(model=model).values_list('model__modelreview', flat=True)

        context['edit_review_btn_txt'] = 1
        context['review_model_id'] = review[0]
    # add a review
    else:
        context['edit_review_btn_txt'] = 0
        context['review_model_id'] = model.pk

    return context
