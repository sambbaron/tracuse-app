# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('watchword', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchwordassociationtype',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='watchwordassociationtype',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 9, 9, 112889, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchworddatumobject',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='watchworddatumobject',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 9, 10, 556972, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchworddatumtype',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='watchworddatumtype',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 9, 11, 966052, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
