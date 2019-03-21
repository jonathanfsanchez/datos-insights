from django import template
from django.core.paginator import Paginator

register = template.Library()


@register.inclusion_tag('reviews/_review_model_list.html', takes_context=True)
def model_reviews_list(context):
    request = context['request']
    model = context['model']

    reviews = model.modelreview_set.all()
    review_page = Paginator(reviews, 6)
    page = request.GET.get('page')

    context['reviews'] = review_page.get_page(page)

    total = reviews.count()

    context['1star'] = reviews.filter(stars=1).count()
    context['2star'] = reviews.filter(stars=2).count()
    context['3star'] = reviews.filter(stars=3).count()
    context['4star'] = reviews.filter(stars=4).count()
    context['5star'] = reviews.filter(stars=5).count()

    if total != 0:
        context['1star_bar'] = round((context['1star'] / total) * 100, 1)
        context['2star_bar'] = round((context['2star'] / total) * 100, 1)
        context['3star_bar'] = round((context['3star'] / total) * 100, 1)
        context['4star_bar'] = round((context['4star'] / total) * 100, 1)
        context['5star_bar'] = round((context['5star'] / total) * 100, 1)

    return context
