# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0007_entitymodel_names_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='associationadjacent',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='associationadjacent',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 6, 408104, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='associationall',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='associationall',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 10, 838358, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='associationdirection',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='associationdirection',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 12, 942478, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='associationtype',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='associationtype',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 14, 749581, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
