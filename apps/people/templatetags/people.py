from django import template

from ..models import Person

register = template.Library()


@register.inclusion_tag("people/includes/people_list.html")
def people():
    """Returns a list of all people

    Returns:
        list of all Person objects
    """

    return {
        'people': Person.objects.all()
    }
