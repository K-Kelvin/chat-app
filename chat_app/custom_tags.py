from django import template

register = template.Library()


@register.simple_tag
def is_sent(message, request):
    return message.sent(request)

@register.filter
def get_profile_pic(user, size=100):
    id = (int(user.id) * 10)
    return f"https://picsum.photos/id/{id}/{size}"