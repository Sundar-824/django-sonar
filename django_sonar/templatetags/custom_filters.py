from django import template

register = template.Library()

@register.filter
def divide(value, divisor):
    try:
        final_duration = f"{float(value) / float(divisor):.2f}"
        return final_duration
    except (ValueError, ZeroDivisionError):
        return None

@register.filter
def date_format(value, format_string):
    try:
        return value.strftime(format_string)
    except (ValueError, TypeError):
        return None

