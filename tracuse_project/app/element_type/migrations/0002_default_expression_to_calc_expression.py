# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elementtype',
            old_name='default_expression',
            new_name='calc_expression',
        ),
    ]
