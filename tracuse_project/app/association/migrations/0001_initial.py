# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssociationAdjacent',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('association_adjacent_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'Associations Adjacent',
                'verbose_name': 'Association Adjacent',
                'ordering': ['sort'],
                'db_table': 'association_adjacent',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssociationAll',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('association_all_id', models.AutoField(serialize=False, primary_key=True)),
                ('distance', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Associations All',
                'verbose_name': 'Association All',
                'ordering': ['sort'],
                'db_table': 'association_all',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssociationDirection',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('entity_name', models.CharField(max_length=25, db_index=True, default='')),
                ('readable_name', models.CharField(max_length=25, db_index=True, default='')),
                ('schema_name', models.CharField(max_length=25, default='')),
                ('readable_plural_name', models.CharField(max_length=25, default='')),
                ('short_definition', models.CharField(max_length=25, blank=True, null=True)),
                ('long_definition', models.CharField(max_length=100, blank=True, null=True)),
                ('association_direction_id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'association_direction',
                'verbose_name': 'Association Direction',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssociationType',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('entity_name', models.CharField(max_length=25, db_index=True, default='')),
                ('readable_name', models.CharField(max_length=25, db_index=True, default='')),
                ('schema_name', models.CharField(max_length=25, default='')),
                ('readable_plural_name', models.CharField(max_length=25, default='')),
                ('short_definition', models.CharField(max_length=25, blank=True, null=True)),
                ('long_definition', models.CharField(max_length=100, blank=True, null=True)),
                ('association_type_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'association_type',
                'verbose_name': 'Association Type',
                'abstract': False,
            },
        ),
    ]
