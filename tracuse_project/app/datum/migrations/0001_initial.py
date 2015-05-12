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
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('entity_name', models.CharField(max_length=25, db_index=True, default='')),
                ('readable_name', models.CharField(max_length=25, db_index=True, default='')),
                ('schema_name', models.CharField(max_length=25, default='')),
                ('readable_plural_name', models.CharField(max_length=25, default='')),
                ('short_definition', models.CharField(max_length=25, blank=True, null=True)),
                ('long_definition', models.CharField(max_length=100, blank=True, null=True)),
                ('datum_group_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'datum_group',
                'verbose_name': 'Datum Group',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DatumObject',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('datum_object_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'datum_object',
                'verbose_name': 'Datum',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='DatumType',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('entity_name', models.CharField(max_length=25, db_index=True, default='')),
                ('readable_name', models.CharField(max_length=25, db_index=True, default='')),
                ('schema_name', models.CharField(max_length=25, default='')),
                ('readable_plural_name', models.CharField(max_length=25, default='')),
                ('short_definition', models.CharField(max_length=25, blank=True, null=True)),
                ('long_definition', models.CharField(max_length=100, blank=True, null=True)),
                ('datum_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('repr_expression', models.CharField(max_length=255)),
                ('datum_group', models.ForeignKey(db_column='datum_group_id', to='datum.DatumGroup')),
            ],
            options={
                'db_table': 'datum_type',
                'verbose_name': 'Datum Type',
                'abstract': False,
            },
        ),
    ]
