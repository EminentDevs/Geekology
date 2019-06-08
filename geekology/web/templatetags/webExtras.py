from django import template

register = template.Library()

@register.filter
def indexTwoList(value,arg):
    if arg == len(value)-1:
        return ''
    else:
        return value[arg+1]

@register.filter
def listFirstElement(value):
    return value[0]

@register.filter
def listElementSkillLabel(value):
    valueList = []
    for item in value:
        valueList.append(item.labelName)
    return valueList
