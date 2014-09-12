from django.views.generic import ListView, DetailView

from .models import Person, Team


class PersonListView(ListView):
    model = Person


class PersonView(DetailView):
    model = Person
    slug_field = 'url_title'
    slug_url_kwarg = 'person_title'


class TeamListView(ListView):
    model = Team


class TeamView(DetailView):
    model = Team
    slug_field = 'url_title'
    slug_url_kwarg = 'team_title'
1
