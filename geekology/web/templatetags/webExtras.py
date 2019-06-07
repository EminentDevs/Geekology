from django import template

register = template.Library()

@register.filter
def indexTwoList(value,arg):
    return value[int(arg)]