# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('datum', '0002_auto_20150512_0854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datumtype',
            old_name='repr_expression',
            new_name='str_expression',
        ),
    ]
