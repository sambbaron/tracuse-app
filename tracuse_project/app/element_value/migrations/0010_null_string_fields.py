# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_value', '0009_basemixin_sort_bigint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementvaluestring',
            name='element_value',
            field=models.CharField(blank=True, max_length=150, default=''),
        ),
        migrations.AlterField(
            model_name='elementvaluetextdata',
            name='element_value',
            field=models.TextField(blank=True, default=''),
        ),
    ]
