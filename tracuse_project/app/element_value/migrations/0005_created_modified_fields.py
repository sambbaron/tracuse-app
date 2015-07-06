# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('element_value', '0004_elementvaluedecimal_default_zero'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementvaluebinary',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='elementvaluebinary',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 32, 151577, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='elementvalueboolean',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='elementvalueboolean',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 33, 721666, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='elementvaluedatetime',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='elementvaluedatetime',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 35, 698779, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='elementvaluedecimal',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='elementvaluedecimal',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 37, 312872, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='elementvaluestring',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='elementvaluestring',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 38, 980165, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='elementvaluetextdata',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='elementvaluetextdata',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 40, 604258, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
