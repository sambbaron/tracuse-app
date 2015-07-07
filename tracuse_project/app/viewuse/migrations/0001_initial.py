# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewuseArrangement',
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
                ('viewuse_arrangement_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Viewuse Arrangement',
                'db_table': 'viewuse_arrangement',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ViewuseDatum',
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
                ('viewuse_datum_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Viewuse Datum',
                'db_table': 'viewuse_datum',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ViewuseObject',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('viewuse_object_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('viewuse_filter', models.TextField(null=True, default='', blank=True)),
                ('user', models.ForeignKey(related_name='viewuse_objects', blank=True, null=True, db_column='user_id', to=settings.AUTH_USER_MODEL)),
                ('viewuse_arrangement', models.ForeignKey(related_name='viewuse_objects', db_column='viewuse_arrangement_id', to='viewuse.ViewuseArrangement')),
                ('viewuse_datum', models.ForeignKey(related_name='viewuse_objects', db_column='viewuse_datum_id', to='viewuse.ViewuseDatum')),
            ],
            options={
                'verbose_name': 'Viewuse Object',
                'db_table': 'viewuse_object',
                'abstract': False,
            },
        ),
    ]
