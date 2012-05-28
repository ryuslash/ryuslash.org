import re

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
def nameless(value):
    return re.sub(r'^(ryuslash|tom)[- ]?', '', value)

register.filter('nameless', nameless)
