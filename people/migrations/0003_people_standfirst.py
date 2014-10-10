# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20140925_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='standfirst',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
