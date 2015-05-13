# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0002_auto_20150512_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='associationdirection',
            name='usage',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='associationtype',
            name='usage',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
