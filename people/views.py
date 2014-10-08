""" Models used by the people app """

from django.views.generic import ListView, DetailView

from .models import Person, Team


class PersonListView(ListView):
    """ Creates a page for all Person('s) """
    model = Person


class PersonView(DetailView):
    """ Creates an individual page for each person """
    model = Person
    slug_field = 'url_title'
    slug_url_kwarg = 'person_title'


class TeamListView(ListView):
    """ Creates a page for all Teams """
    model = Team


class TeamView(DetailView):
    """ Creates an individual page for each team """
    model = Team
    slug_field = 'url_title'
    slug_url_kwarg = 'team_title'
