# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0002_auto_20150424_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datumgroup',
            name='name',
            field=models.CharField(default='', max_length=25, db_index=True),
        ),
    ]
