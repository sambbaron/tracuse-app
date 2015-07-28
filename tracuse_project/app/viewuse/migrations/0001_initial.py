# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewuseArrangement',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('entity_name', models.CharField(db_index=True, max_length=40, default='')),
                ('schema_name', models.CharField(blank=True, default='', null=True, max_length=40)),
                ('readable_name', models.CharField(blank=True, db_index=True, null=True, max_length=40, default='')),
                ('readable_plural_name', models.CharField(blank=True, default='', null=True, max_length=40)),
                ('short_definition', models.CharField(blank=True, null=True, max_length=25)),
                ('long_definition', models.CharField(blank=True, null=True, max_length=100)),
                ('example', models.CharField(blank=True, null=True, max_length=100)),
                ('viewuse_arrangement_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
                'db_table': 'viewuse_arrangement',
                'verbose_name': 'Viewuse Arrangement',
            },
        ),
        migrations.CreateModel(
            name='ViewuseObject',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, default='Blank ', null=True, max_length=100)),
                ('description', models.CharField(blank=True, null=True, max_length=255)),
                ('datum_filter', models.TextField(blank=True, default='', null=True)),
                ('viewuse_object_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(blank=True, null=True, db_column='user_id', to=settings.AUTH_USER_MODEL)),
                ('viewuse_arrangement', models.ForeignKey(to='viewuse.ViewuseArrangement', db_column='viewuse_arrangement_id')),
            ],
            options={
                'abstract': False,
                'default_related_name': 'viewuse_objects',
                'db_table': 'viewuse_object',
                'verbose_name': 'Viewuse Object',
                'ordering': ['sort'],
            },
        ),
    ]
