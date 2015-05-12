# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0011_basemixin_sort_bigint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filterruleassociation',
            old_name='depth',
            new_name='distance',
        ),
    ]
