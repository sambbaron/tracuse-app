# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datumgroup',
            name='active',
            field=models.BooleanField(default=True, db_index=True),
        ),
        migrations.AddField(
            model_name='datumgroup',
            name='long_definition',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='datumgroup',
            name='name',
            field=models.CharField(unique=True, default='', db_index=True, max_length=25),
        ),
        migrations.AddField(
            model_name='datumgroup',
            name='short_definition',
            field=models.CharField(null=True, max_length=25, blank=True),
        ),
        migrations.AddField(
            model_name='datumgroup',
            name='sort',
            field=models.IntegerField(default=0, db_index=True),
        ),
    ]
