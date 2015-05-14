# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('datum', '0004_entity_add_field_usage'),
    ]

    operations = [
        migrations.AddField(
            model_name='datumgroup',
            name='example',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='datumtype',
            name='example',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
    ]
