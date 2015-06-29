# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0008_remove_viewusefilter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewuseobject',
            name='entity_name',
        ),
        migrations.RemoveField(
            model_name='viewuseobject',
            name='example',
        ),
        migrations.RemoveField(
            model_name='viewuseobject',
            name='filter_set',
        ),
        migrations.RemoveField(
            model_name='viewuseobject',
            name='long_definition',
        ),
        migrations.RemoveField(
            model_name='viewuseobject',
            name='readable_name',
        ),
        migrations.RemoveField(
            model_name='viewuseobject',
            name='readable_plural_name',
        ),
        migrations.RemoveField(
            model_name='viewuseobject',
            name='schema_name',
        ),
        migrations.RemoveField(
            model_name='viewuseobject',
            name='short_definition',
        ),
        migrations.AddField(
            model_name='viewuseobject',
            name='description',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='viewuseobject',
            name='title',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
    ]
