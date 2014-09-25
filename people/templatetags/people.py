from django import template

from ..models import Person

register = template.Library()


@register.inclusion_tag("people/includes/people_list.html")
def people():

    return {
        'people': Person.objects.all()
    }
