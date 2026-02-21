from django import template

register = template.Library()

@register.filter
def naira(value):
    try:
        value = int(value)
    except (TypeError, ValueError):
        return value
    return f"{value:,}"
