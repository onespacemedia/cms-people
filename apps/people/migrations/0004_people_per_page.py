# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_people_standfirst'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='per_page',
            field=models.IntegerField(default=5, null=True, verbose_name=b'people per page', blank=True),
            preserve_default=True,
        ),
    ]
