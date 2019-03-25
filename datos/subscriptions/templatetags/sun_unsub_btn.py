from django import template

register = template.Library()


@register.inclusion_tag('subscriptions/sub_unsub_btn.html', takes_context=True)
def get_sub_unsub_btn(context, model):
    request = context['request']

    context['banner_btn_icon'] = "add_shopping_cart"
    context['banner_btn_page'] = 'subscriptions/subscription_model_form.html'
    context['banner_btn_text'] = "Subscribe"

    # show to guests and logged in users - only change these links when they are already logged & subscribed
    if request.user.is_authenticated:
        if model.modelsubscription_set.filter(customer=request.user.id).filter(date_unsubscribed__isnull=True).exists():
            context['banner_btn_icon'] = "remove_shopping_cart"
            context['banner_btn_page'] = 'subscriptions/unsubscribe_model_form.html'
            context['banner_btn_text'] = "Unsubscribe"

    return context
