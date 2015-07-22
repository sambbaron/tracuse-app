# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UiArrangementType',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('entity_name', models.CharField(max_length=40, db_index=True, default='')),
                ('schema_name', models.CharField(max_length=40, blank=True, default='', null=True)),
                ('readable_name', models.CharField(max_length=40, blank=True, default='', db_index=True, null=True)),
                ('readable_plural_name', models.CharField(max_length=40, blank=True, default='', null=True)),
                ('short_definition', models.CharField(max_length=25, blank=True, null=True)),
                ('long_definition', models.CharField(max_length=100, blank=True, null=True)),
                ('example', models.CharField(max_length=100, blank=True, null=True)),
                ('ui_arrangement_type_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'ui_arrangement_type',
                'abstract': False,
                'verbose_name': 'Arrangement Type',
            },
        ),
        migrations.CreateModel(
            name='UiFormattingType',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('entity_name', models.CharField(max_length=40, db_index=True, default='')),
                ('schema_name', models.CharField(max_length=40, blank=True, default='', null=True)),
                ('readable_name', models.CharField(max_length=40, blank=True, default='', db_index=True, null=True)),
                ('readable_plural_name', models.CharField(max_length=40, blank=True, default='', null=True)),
                ('short_definition', models.CharField(max_length=25, blank=True, null=True)),
                ('long_definition', models.CharField(max_length=100, blank=True, null=True)),
                ('example', models.CharField(max_length=100, blank=True, null=True)),
                ('ui_formatting_type_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'ui_formatting_type',
                'abstract': False,
                'verbose_name': 'Formatting Type',
            },
        ),
    ]
