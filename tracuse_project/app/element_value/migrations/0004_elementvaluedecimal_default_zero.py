# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_value', '0003_element_value_rename_elvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementvaluedecimal',
            name='elvalue',
            field=models.DecimalField(blank=True, default=0, null=True, max_digits=10, decimal_places=2),
        ),
    ]
