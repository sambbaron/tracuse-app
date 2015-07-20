# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viewuse', '0005_viewuse_renamefilter'),
    ]

    operations = [
        migrations.CreateModel(
            name='WindowuseObject',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('windowuse_object_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, blank=True, null=True)),
                ('description', models.CharField(max_length=255, blank=True, null=True)),
                ('datum_filter', models.TextField(blank=True, default='', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column='user_id', blank=True, null=True)),
            ],
            options={
                'db_table': 'windowuse_object',
                'verbose_name': 'Windowuse Object',
                'ordering': ['sort'],
                'abstract': False,
                'default_related_name': 'windowuse_objects',
            },
        ),
        migrations.CreateModel(
            name='WindowuseViewuse',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('windowuse_viewuse_id', models.AutoField(primary_key=True, serialize=False)),
                ('viewuse_object', models.ForeignKey(to='viewuse.ViewuseObject', db_column='viewuse_object_id')),
                ('windowuse_object', models.ForeignKey(to='windowuse.WindowuseObject', db_column='windowuse_object_id')),
            ],
            options={
                'db_table': 'windowuse_viewuse',
                'verbose_name': 'Windowuse Viewuse',
                'ordering': ['sort'],
                'abstract': False,
                'default_related_name': 'windowuse_viewuses',
            },
        ),
    ]
