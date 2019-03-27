from django import template

register = template.Library()


@register.inclusion_tag('users/_model_bookmark.html', takes_context=True)
def get_model_bookmark_state(context, model):
    request = context['request']

    # show to guests and logged in users - only change these links when they are already logged & subscribed
    if request.user.is_authenticated:
        if model.datosuser_set.filter(pk=request.user.id).exists():
            # is bookmarked
            context['bookmark_to_render'] = 'bookmark'
        else:
            context['bookmark_to_render'] = 'bookmark_border'

    return context

# def get_dataset_bookmark_state():
#     pass
