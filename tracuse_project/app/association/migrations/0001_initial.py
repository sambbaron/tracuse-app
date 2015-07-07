# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssociationAdjacent',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('association_adjacent_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Associations Adjacent',
                'db_table': 'association_adjacent',
                'verbose_name': 'Association Adjacent',
                'ordering': ['sort'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssociationAll',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('association_all_id', models.AutoField(primary_key=True, serialize=False)),
                ('distance', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Associations All',
                'db_table': 'association_all',
                'verbose_name': 'Association All',
                'ordering': ['sort'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssociationDirection',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('entity_name', models.CharField(max_length=40, default='', db_index=True)),
                ('schema_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('readable_name', models.CharField(max_length=40, default='', blank=True, db_index=True, null=True)),
                ('readable_plural_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('short_definition', models.CharField(max_length=25, null=True, blank=True)),
                ('long_definition', models.CharField(max_length=100, null=True, blank=True)),
                ('example', models.CharField(max_length=100, null=True, blank=True)),
                ('association_direction_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Association Direction',
                'db_table': 'association_direction',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssociationType',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('entity_name', models.CharField(max_length=40, default='', db_index=True)),
                ('schema_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('readable_name', models.CharField(max_length=40, default='', blank=True, db_index=True, null=True)),
                ('readable_plural_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('short_definition', models.CharField(max_length=25, null=True, blank=True)),
                ('long_definition', models.CharField(max_length=100, null=True, blank=True)),
                ('example', models.CharField(max_length=100, null=True, blank=True)),
                ('association_type_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Association Type',
                'db_table': 'association_type',
                'abstract': False,
            },
        ),
    ]
