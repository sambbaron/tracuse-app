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
                'verbose_name_plural': 'Associations Adjacent',
                'verbose_name': 'Association Adjacent',
                'db_table': 'association_adjacent',
                'abstract': False,
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
                'verbose_name_plural': 'Associations All',
                'verbose_name': 'Association All',
                'db_table': 'association_all',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssociationDirection',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, max_length=25, blank=True)),
                ('long_definition', models.CharField(null=True, max_length=100, blank=True)),
                ('association_direction_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Association Direction',
                'db_table': 'association_direction',
            },
        ),
        migrations.CreateModel(
            name='AssociationType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, max_length=25, blank=True)),
                ('long_definition', models.CharField(null=True, max_length=100, blank=True)),
                ('association_type_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Association Type',
                'db_table': 'association_type',
            },
        ),
    ]
