# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatumGroup',
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
                ('datum_group_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Datum Group',
                'db_table': 'datum_group',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DatumObject',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('datum_object_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Datum',
                'db_table': 'datum_object',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='DatumType',
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
                ('datum_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('title_expression', models.CharField(max_length=255)),
                ('icon_class', models.CharField(max_length=25, null=True, blank=True)),
                ('datum_group', models.ForeignKey(related_name='datum_types', db_column='datum_group_id', to='datum.DatumGroup')),
            ],
            options={
                'verbose_name': 'Datum Type',
                'db_table': 'datum_type',
                'abstract': False,
            },
        ),
    ]
