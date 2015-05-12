# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchword', '0008_basemixin_ordering_remove_str'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchwordassociationtype',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='watchworddatumobject',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='watchworddatumtype',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
    ]
