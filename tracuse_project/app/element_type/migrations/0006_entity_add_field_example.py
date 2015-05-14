# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('element_type', '0005_entity_add_field_usage'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementdatatype',
            name='example',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='elementoption',
            name='example',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='elementtype',
            name='example',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
    ]
