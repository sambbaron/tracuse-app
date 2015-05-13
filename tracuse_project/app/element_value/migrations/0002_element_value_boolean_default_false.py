# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_value', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementvalueboolean',
            name='element_value',
            field=models.BooleanField(default=False),
        ),
    ]
