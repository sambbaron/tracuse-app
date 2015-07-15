# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0002_viewusenested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewusenested',
            name='nested_viewuse',
            field=models.ForeignKey(db_column='nested_viewuse_id', related_name='parent_viewuses', to='viewuse.ViewuseObject'),
        ),
        migrations.AlterField(
            model_name='viewusenested',
            name='parent_viewuse',
            field=models.ForeignKey(db_column='parent_viewuse_id', related_name='nested_viewuses', to='viewuse.ViewuseObject'),
        ),
    ]
