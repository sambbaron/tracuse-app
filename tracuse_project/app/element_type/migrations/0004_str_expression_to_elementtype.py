# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('element_type', '0003_calc_expression_and_str_expression'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementdatumtype',
            name='str_expression',
        ),
        migrations.AddField(
            model_name='elementtype',
            name='str_expression',
            field=models.CharField(default='', blank=True, max_length=255),
        ),
    ]
