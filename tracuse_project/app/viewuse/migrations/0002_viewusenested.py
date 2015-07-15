# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewuseNested',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('viewuse_nested_id', models.AutoField(primary_key=True, serialize=False)),
                ('order', models.IntegerField(default=1)),
                ('height', models.CharField(max_length=4, default='auto')),
                ('width', models.CharField(max_length=4, default='auto')),
                ('nested_viewuse', models.ForeignKey(db_column='nested_viewuse_id', to='viewuse.ViewuseObject', related_name='nested_viewuses')),
                ('parent_viewuse', models.ForeignKey(db_column='parent_viewuse_id', to='viewuse.ViewuseObject', related_name='parent_viewuses')),
            ],
            options={
                'db_table': 'viewuse_nested',
                'abstract': False,
                'verbose_name': 'Nested Viewuse',
                'verbose_name_plural': 'Nested Viewuses',
            },
        ),
    ]
