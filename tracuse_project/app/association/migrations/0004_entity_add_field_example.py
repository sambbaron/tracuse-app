# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('association', '0003_entity_add_field_usage'),
    ]

    operations = [
        migrations.AddField(
            model_name='associationdirection',
            name='example',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='associationtype',
            name='example',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
    ]
