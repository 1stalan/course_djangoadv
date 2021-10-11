from django import template
from django.utils import timezone

now = timezone.now()

register = template.Library()

@register.simple_tag
def current_time(format_string):
    # return datetime.now().strftime(format_string)
    return now
@register.simple_tag
def footer_message():
    import django
    return 'Desenvolvimento Web com Django ' + str(django.get_version()
)