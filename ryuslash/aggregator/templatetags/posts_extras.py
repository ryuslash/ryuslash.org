import re

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
def nameless(value):
    return re.sub(r'(^|by[- ])(ryuslash|tom)[- ]?', '', value)

@stringfilter
def truncate(value, length):
    if len(value) > length:
        value = value[:length-3] + '...'

    return value

register.filter('nameless', nameless)
register.filter('truncate', truncate)
