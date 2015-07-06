# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0014_elementtype_element_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementdatatype',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='elementdatatype',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 22, 548027, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='elementdatumobject',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='elementdatumobject',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 24, 415134, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='elementdatumtype',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='elementdatumtype',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 25, 981224, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='elementoperator',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='elementoperator',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 27, 496310, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='elementoption',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='elementoption',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 29, 13397, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='elementtype',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='elementtype',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 30, 550485, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
