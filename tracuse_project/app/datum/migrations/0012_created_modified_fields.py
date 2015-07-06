# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0011_datumtype_icon_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='datumgroup',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='datumgroup',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 16, 544684, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datumobject',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 18, 293784, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datumtype',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='datumtype',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 20, 41884, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
