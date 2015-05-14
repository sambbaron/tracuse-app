# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('association', '0004_entity_add_field_example'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='associationdirection',
            name='usage',
        ),
        migrations.RemoveField(
            model_name='associationtype',
            name='usage',
        ),
    ]
