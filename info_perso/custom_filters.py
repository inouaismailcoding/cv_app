from django import template

register = template.Library()

@register.filter
def multiplication(value, multiplicateur):
    return value * multiplicateur

@register.filter
def appreciation(value):
    value=int(value)
    if value == 4 or value == 5 or value == 6:
        return 'passable'
    elif value == 7 :
        return 'Bien'
    elif value ==8:
        return 'Tres Bien'
    elif value == 9 or value==10:
        return 'excellent'