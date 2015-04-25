# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0003_auto_20150424_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatumType',
            fields=[
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('name', models.CharField(max_length=25, db_index=True, default='')),
                ('short_definition', models.CharField(max_length=25, blank=True, null=True)),
                ('long_definition', models.CharField(max_length=100, blank=True, null=True)),
                ('datum_type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('datum_group', models.ForeignKey(db_column='datum_group_id', to='datum.DatumGroup')),
            ],
            options={
                'db_table': 'datum_type',
                'abstract': False,
            },
        ),
    ]
