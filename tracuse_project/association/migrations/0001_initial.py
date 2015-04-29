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
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('association_adjacent_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'association_adjacent',
                'abstract': False,
                'verbose_name': 'Association Adjacent',
                'verbose_name_plural': 'Associations Adjacent',
            },
        ),
        migrations.CreateModel(
            name='AssociationAll',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('association_all_id', models.AutoField(serialize=False, primary_key=True)),
                ('depth', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'association_all',
                'abstract': False,
                'verbose_name': 'Association All',
                'verbose_name_plural': 'Associations All',
            },
        ),
        migrations.CreateModel(
            name='AssociationDirection',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('association_direction_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'association_direction',
                'abstract': False,
                'verbose_name': 'Association Direction',
            },
        ),
        migrations.CreateModel(
            name='AssociationType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('association_type_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'association_type',
                'abstract': False,
                'verbose_name': 'Association Type',
            },
        ),
    ]
