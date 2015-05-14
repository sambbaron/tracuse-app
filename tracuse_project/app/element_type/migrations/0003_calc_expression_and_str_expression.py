# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('element_type', '0002_default_expression_to_calc_expression'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementtype',
            name='calc_expression',
        ),
        migrations.AddField(
            model_name='elementdatumtype',
            name='calc_expression',
            field=models.CharField(default='', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='elementdatumtype',
            name='str_expression',
            field=models.CharField(default='', max_length=255, blank=True),
        ),
    ]
