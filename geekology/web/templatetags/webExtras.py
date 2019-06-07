from django import template

register = template.Library()

@register.filter
def indexTwoList(value,arg):
    print(arg)
    if arg == len(value)-1:
        return ''
    else:
        return value[arg+1]