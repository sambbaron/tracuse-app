# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('filter', '0002_entity_add_field_usage'),
    ]

    operations = [
        migrations.AddField(
            model_name='filterset',
            name='example',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
    ]
