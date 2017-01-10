from django.views.generic import DetailView, ListView

from .models import Person, Team


class PersonListView(ListView):
    model = Person

    def get_paginate_by(self, queryset):
        return self.request.pages.current.content.per_page

    def get_queryset(self):
        queryset = super(PersonListView, self).get_queryset()
        return queryset.filter(page__page=self.request.pages.current)


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
