# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0005_viewuse_renamefilter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewusenested',
            name='nested_viewuse',
        ),
        migrations.RemoveField(
            model_name='viewusenested',
            name='parent_viewuse',
        ),
        migrations.DeleteModel(
            name='ViewuseNested',
        ),
    ]
