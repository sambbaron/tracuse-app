# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viewuse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WindowuseObject',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, default='Blank ', null=True, max_length=100)),
                ('description', models.CharField(blank=True, null=True, max_length=255)),
                ('datum_filter', models.TextField(blank=True, default='', null=True)),
                ('windowuse_object_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(blank=True, null=True, db_column='user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'default_related_name': 'windowuse_objects',
                'db_table': 'windowuse_object',
                'verbose_name': 'Windowuse Object',
                'ordering': ['sort'],
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
                'abstract': False,
                'default_related_name': 'windowuse_viewuses',
                'db_table': 'windowuse_viewuse',
                'verbose_name': 'Windowuse Viewuse',
                'ordering': ['sort'],
            },
        ),
    ]
