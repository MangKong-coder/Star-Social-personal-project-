from django import template

register = template.Library()

def change(value, arg):
    return value.replace(value, arg)

def add(value):
    if value > 10:
        return value + 20
    else:
        return value - 20

register.filter('change', change)
register.filter('plus', add)