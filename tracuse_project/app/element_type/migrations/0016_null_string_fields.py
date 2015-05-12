# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0015_basemixin_sort_bigint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementtype',
            name='default_expression',
            field=models.CharField(blank=True, max_length=255, default=''),
        ),
    ]
