from django import template

from models.models import Model

register = template.Library()


@register.inclusion_tag('models/model_banner_full.html', takes_context=True)
def display_full_banner(context, model_id):
    request = context['request']

    model = Model.objects.get(pk=model_id)

    context['banner_btn_icon'] = "add_shopping_cart"
    context['banner_btn_page'] = 'subscriptions/subscription_model_form.html'
    context['banner_btn_text'] = "Subscribe"

    # show to guests and logged in users - only change these links when they are already logged & subscribed
    if request.user.is_authenticated:
        if model.modelsubscription_set.filter(customer=request.user.id).filter(date_unsubscribed__isnull=True).exists():
            context['banner_btn_icon'] = "remove_shopping_cart"
            context['banner_btn_page'] = 'subscriptions/unsubscribe_model_form.html'
            context['banner_btn_text'] = "Unsubscribe"

        if model.datosuser_set.filter(pk=request.user.id).exists():
            # is bookmarked
            context['bookmark_to_render'] = 'bookmark'
        else:
            context['bookmark_to_render'] = 'bookmark_border'

    return context
