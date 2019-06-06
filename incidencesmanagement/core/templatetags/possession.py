from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
@stringfilter
def possession(value):
    print(value[-1])
    return f"{value}'" if value[-1] == "s" or value[-1] == "S" else f"{value}'s"

