from django import template
from django.utils.safestring import mark_safe

register = template.Library()

star = '<i class="material-icons text-warning" style="font-size: {font_size}px ">star</i>'
half_star = '<i class="material-icons text-warning" style="font-size: {font_size}px ">star_half</i>'
star_border = '<i class="material-icons text-warning" style="font-size: {font_size}px ">star_border</i>'


@register.simple_tag
def get_ratings(rating, font_size=24):
    if rating is None:
        return mark_safe('No Reviews')

    html_ratings = ''

    for i in range(1, 6):
        i_val = i - rating

        if i_val <= 0:
            html_ratings += star.format(font_size=font_size)
        elif 0 < i_val < 1:
            html_ratings += half_star.format(font_size=font_size)
        else:
            html_ratings += star_border.format(font_size=font_size)

    return mark_safe(html_ratings)
