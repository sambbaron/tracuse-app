# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementtypedatumtype',
            name='entity_name',
        ),
        migrations.RemoveField(
            model_name='elementtypedatumtype',
            name='long_definition',
        ),
        migrations.RemoveField(
            model_name='elementtypedatumtype',
            name='short_definition',
        ),
    ]
