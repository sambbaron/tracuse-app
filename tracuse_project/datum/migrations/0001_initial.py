# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatumGroup',
            fields=[
                ('datum_group_id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'datum_group',
            },
        ),
    ]
