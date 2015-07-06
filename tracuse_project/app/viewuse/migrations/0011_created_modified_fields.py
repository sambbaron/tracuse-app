# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0010_viewusefilter_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewusearrangement',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='viewusearrangement',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 9, 4, 866646, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viewusedatum',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='viewusedatum',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 9, 6, 263726, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viewuseobject',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='viewuseobject',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 9, 7, 690808, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
