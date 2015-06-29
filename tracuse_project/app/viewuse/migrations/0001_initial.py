# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0015_filterruledatatype_filtersetdatatyperule'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewuseArrangement',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('entity_name', models.CharField(max_length=40, default='', db_index=True)),
                ('schema_name', models.CharField(max_length=40, default='')),
                ('readable_name', models.CharField(max_length=40, default='', db_index=True)),
                ('readable_plural_name', models.CharField(max_length=40, default='')),
                ('short_definition', models.CharField(null=True, max_length=25, blank=True)),
                ('long_definition', models.CharField(null=True, max_length=100, blank=True)),
                ('example', models.CharField(null=True, max_length=100, blank=True)),
                ('viewuse_arrangement_id', models.AutoField(serialize=False, primary_key=True)),
                ('template_path', models.CharField(unique=True, max_length=40, default='')),
            ],
            options={
                'verbose_name': 'Viewuse Arrangement',
                'abstract': False,
                'db_table': 'viewuse_arrangement',
            },
        ),
        migrations.CreateModel(
            name='ViewuseFilter',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('entity_name', models.CharField(max_length=40, default='', db_index=True)),
                ('schema_name', models.CharField(max_length=40, default='')),
                ('readable_name', models.CharField(max_length=40, default='', db_index=True)),
                ('readable_plural_name', models.CharField(max_length=40, default='')),
                ('short_definition', models.CharField(null=True, max_length=25, blank=True)),
                ('long_definition', models.CharField(null=True, max_length=100, blank=True)),
                ('example', models.CharField(null=True, max_length=100, blank=True)),
                ('viewuse_filter_id', models.AutoField(serialize=False, primary_key=True)),
                ('viewuse_filter', models.CharField(max_length=255, default='')),
                ('filter_set', models.ForeignKey(db_column='filter_set_id', related_name='viewuse_filters', to='filter.FilterSet')),
                ('viewuse_arrangement', models.ForeignKey(db_column='viewuse_arrangement_id', related_name='viewuse_filters', to='viewuse.ViewuseArrangement')),
            ],
            options={
                'verbose_name': 'Viewuse Filter',
                'abstract': False,
                'db_table': 'viewuse_filter',
            },
        ),
        migrations.CreateModel(
            name='ViewuseObject',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('entity_name', models.CharField(max_length=40, default='', db_index=True)),
                ('schema_name', models.CharField(max_length=40, default='')),
                ('readable_name', models.CharField(max_length=40, default='', db_index=True)),
                ('readable_plural_name', models.CharField(max_length=40, default='')),
                ('short_definition', models.CharField(null=True, max_length=25, blank=True)),
                ('long_definition', models.CharField(null=True, max_length=100, blank=True)),
                ('example', models.CharField(null=True, max_length=100, blank=True)),
                ('viewuse_object_id', models.AutoField(serialize=False, primary_key=True)),
                ('viewuse_arrangement', models.ForeignKey(db_column='viewuse_arrangement_id', related_name='viewuse_objects', to='viewuse.ViewuseArrangement')),
            ],
            options={
                'verbose_name': 'Viewuse Object',
                'abstract': False,
                'db_table': 'viewuse_object',
            },
        ),
    ]
