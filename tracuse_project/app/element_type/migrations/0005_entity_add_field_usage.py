# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0004_str_expression_to_elementtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementdatatype',
            name='usage',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='elementoption',
            name='usage',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='elementtype',
            name='usage',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
