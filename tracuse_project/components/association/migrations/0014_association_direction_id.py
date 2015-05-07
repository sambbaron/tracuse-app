# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0013_rename_depth_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associationdirection',
            name='association_direction_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
