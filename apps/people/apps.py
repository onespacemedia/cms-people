from cms.models import PageBaseSearchAdapter
from django.apps import AppConfig
from watson import search as watson


class PeopleConfig(AppConfig):
    name = 'people'

    def ready(self):
        Person = self.get_model('Person')
        watson.register(Person, adapter_cls=PageBaseSearchAdapter)
