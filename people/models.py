from django.db import models

from cms.models import SearchMetaBase, HtmlField
from cms.apps.pages.models import ContentBase, PageBase, Page
from cms.apps.media.models import ImageRefField


class Team(PageBase):

    """A team for people to be a part of."""

    content_primary = HtmlField(
        "primary content",
        blank=True
    )

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class People(ContentBase):
    header_text = HtmlField(
        blank=True,
        null=True
    )
    footer_text = HtmlField(
        blank=True,
        null=True
    )
    urlconf = "people.urls"


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
        null=True,
        blank=True
    )
    photo = ImageRefField(
        blank=True,
        null=True
    )
    bio = models.TextField(
        blank=True,
        null=True
    )
    url_title = models.CharField(
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

    def __unicode__(self):
        return "{} {}".format(
            self.first_name,
            self.last_name
        )

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "people"

    def get_absolute_url(self):
        return "{}{}/".format(
            self.page.page.get_absolute_url(),
            self.url_title
        )
