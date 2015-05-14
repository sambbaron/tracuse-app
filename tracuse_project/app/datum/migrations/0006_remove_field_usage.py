# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('datum', '0005_entity_add_field_example'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datumgroup',
            name='usage',
        ),
        migrations.RemoveField(
            model_name='datumtype',
            name='usage',
        ),
    ]
