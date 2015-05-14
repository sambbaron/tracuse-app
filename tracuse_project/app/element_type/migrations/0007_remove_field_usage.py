# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('element_type', '0006_entity_add_field_example'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementdatatype',
            name='usage',
        ),
        migrations.RemoveField(
            model_name='elementoption',
            name='usage',
        ),
        migrations.RemoveField(
            model_name='elementtype',
            name='usage',
        ),
    ]
