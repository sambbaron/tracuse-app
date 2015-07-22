# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ui_object', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewuseObject',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, blank=True, null=True)),
                ('description', models.CharField(max_length=255, blank=True, null=True)),
                ('datum_filter', models.TextField(blank=True, default='', null=True)),
                ('viewuse_object_id', models.AutoField(primary_key=True, serialize=False)),
                ('ui_arrangement_type', models.ForeignKey(blank=True, db_column='ui_arrangement_type_id', to='ui_object.UiArrangementType', null=True)),
                ('ui_formatting_type', models.ForeignKey(blank=True, db_column='ui_formatting_type_id', to='ui_object.UiFormattingType', null=True)),
                ('user', models.ForeignKey(blank=True, db_column='user_id', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'viewuse_object',
                'verbose_name': 'Viewuse Object',
                'abstract': False,
                'ordering': ['sort'],
                'default_related_name': 'viewuse_objects',
            },
        ),
    ]
