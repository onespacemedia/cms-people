# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('order',), 'verbose_name_plural': 'people'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={},
        ),
        migrations.RemoveField(
            model_name='people',
            name='footer_text',
        ),
        migrations.RemoveField(
            model_name='people',
            name='header_text',
        ),
        migrations.AddField(
            model_name='person',
            name='order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=cms.models.fields.HtmlField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='page',
            field=models.ForeignKey(to='pages.Page'),
        ),
        migrations.AlterField(
            model_name='person',
            name='url_title',
            field=models.CharField(unique=True, max_length=256, verbose_name=b'URL title'),
        ),
    ]
