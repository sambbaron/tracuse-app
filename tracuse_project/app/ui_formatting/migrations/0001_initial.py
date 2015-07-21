# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UiFormattingGeneric',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ui_object_id', models.IntegerField()),
                ('ui_formatting_generic_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'Formatting Generic Options',
                'db_table': 'ui_formatting_generic',
                'abstract': False,
                'ordering': ['sort'],
                'verbose_name': 'Formatting Generic Options',
            },
        ),
        migrations.CreateModel(
            name='UiFormattingType',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('entity_name', models.CharField(db_index=True, max_length=40, default='')),
                ('schema_name', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('readable_name', models.CharField(blank=True, db_index=True, default='', max_length=40, null=True)),
                ('readable_plural_name', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('short_definition', models.CharField(blank=True, max_length=25, null=True)),
                ('long_definition', models.CharField(blank=True, max_length=100, null=True)),
                ('example', models.CharField(blank=True, max_length=100, null=True)),
                ('ui_formatting_type_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'ui_formatting_type',
                'abstract': False,
                'verbose_name': 'Formatting Type',
            },
        ),
    ]
