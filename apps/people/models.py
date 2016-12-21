from cms.apps.media.models import ImageRefField
from cms.apps.pages.models import ContentBase, PageBase
from cms.models import HtmlField, SearchMetaBase
from django.db import models


class Team(PageBase):
    content_primary = HtmlField(
        'primary content',
        blank=True
    )

    def __unicode__(self):
        return self.title


class People(ContentBase):
    # The heading that the admin places this content under.
    classifier = 'apps'

    # The urlconf used to power this content's views.
    urlconf = '{{ project_name }}.apps.people.urls'

    standfirst = models.TextField(
        blank=True,
        null=True
    )

    per_page = models.IntegerField(
        'people per page',
        default=5,
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.page.title


class Person(SearchMetaBase):
    page = models.ForeignKey(
        People
    )

    title = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

    first_name = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

    middle_name = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

    job_title = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

    teams = models.ManyToManyField(
        Team,
        blank=True
    )

    photo = ImageRefField(
        blank=True,
        null=True
    )

    bio = HtmlField(
        blank=True,
        null=True
    )

    url_title = models.CharField(
        'URL title',
        max_length=256,
        unique=True
    )

    email = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    linkedin_username = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    skype_username = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    twitter_username = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'people'

    def __unicode__(self):
        fields = ['title', 'first_name', 'middle_name', 'last_name']
        parts = [getattr(self, field) for field in fields if getattr(self, field)]
        return u' '.join(parts)

    def get_absolute_url(self):
        return self.page.page.reverse('person', kwargs={
            'person_title': self.url_title,
        })

    def get_twitter_url(self):
        twitter_username = self.twitter_username

        if twitter_username.startswith('http://') or twitter_username.startswith('https://'):
            return self.twitter_username

        if self.twitter_username.startswith('@'):
            twitter_username = twitter_username[1:]

        return u"https://twitter.com/{}".format(twitter_username)
