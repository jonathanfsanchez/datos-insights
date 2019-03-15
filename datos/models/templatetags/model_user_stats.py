from django import template

from models.models import Model

register = template.Library()


@register.simple_tag(takes_context=True)
def get_user_api_calls(context, model):
    request = context['request']

    api_calls = None

    if request.user.id == model.user.id:
        # all users api calls
        api_calls = model.get_total_api_calls()
    else:
        api_calls = model.get_total_api_calls_by_customer(request.user.id)

    return api_calls


@register.simple_tag(takes_context=True)
def get_user_api_avg_time(context, model):
    request = context['request']

    api_calls_avg = ''

    if request.user.id == model.user.id:
        # all users api calls
        api_calls_avg = model.get_avg_api_calls()
    else:
        api_calls_avg = model.get_avg_api_calls_by_customer(request.user.id)

    return api_calls_avg
