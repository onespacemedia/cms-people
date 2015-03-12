""" Models used by the people app """
from django.db import models

from cms.models import SearchMetaBase, HtmlField
from cms.apps.pages.models import ContentBase, PageBase, Page
from cms.apps.media.models import ImageRefField


class Team(PageBase):
    """ A team for Person's to be a part of """

    content_primary = HtmlField(
        "primary content",
        blank=True
    )


class People(ContentBase):
    """ A base for Person's """

    # The heading that the admin places this content under.
    classifier = "apps"

    # The urlconf used to power this content's views.
    urlconf = "{{ project_name }}.apps.people.urls"

    standfirst = models.TextField(
        blank=True,
        null=True
    )

    per_page = models.IntegerField(
        "people per page",
        default=5,
        blank=True,
        null=True
    )


class Person(SearchMetaBase):
    """ A person """

    page = models.ForeignKey(
        Page
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
        null=True,
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
        "URL title",
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
        ordering = ('order',)
        verbose_name_plural = "people"

    def __unicode__(self):
        return u"{} {}".format(
            self.first_name,
            self.last_name
        )

    def get_absolute_url(self):
        """ Gets the url of Person

        Returns:
            url of Person

        """
        return "{}{}/".format(
            self.page.get_absolute_url(),
            self.url_title
        )
