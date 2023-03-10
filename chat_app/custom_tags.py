from django import template

register = template.Library()


@register.simple_tag
def is_sent(message, request):
    return message.sent(request)
