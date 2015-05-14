# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('filter', '0003_entity_add_field_example'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filterset',
            name='usage',
        ),
    ]
