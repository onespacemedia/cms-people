""" Models used by the people app """
from django.views.generic import ListView, DetailView

from .models import Person, Team


class PersonListView(ListView):
    """ A list of all Person's """
    model = Person


class PersonView(DetailView):
    """ An individual Person """
    model = Person
    slug_field = 'url_title'
    slug_url_kwarg = 'person_title'


class TeamListView(ListView):
    """ A list of all Teams """
    model = Team


class TeamView(DetailView):
    """ An individual Team """
    model = Team
    slug_field = 'url_title'
    slug_url_kwarg = 'team_title'
