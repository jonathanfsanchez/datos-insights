from django import template

register = template.Library()


@register.inclusion_tag('models/model_banner_full.html', takes_context=True)
def display_full_banner(context):
    request = context['request']
    model = context['model']

    # show to guests and logged in users - only change these links when they are already logged & subscribed
    if request.user.is_authenticated:
        if model.datosuser_set.filter(pk=request.user.id).exists():
            # is bookmarked
            context['bookmark_to_render'] = 'bookmark'
        else:
            context['bookmark_to_render'] = 'bookmark_border'

    return context
