# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0013_basemixin_ordering_remove_str'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datumgroup',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='datumobject',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='datumtype',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
    ]
