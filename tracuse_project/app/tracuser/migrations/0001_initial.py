# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TracuserLanding',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('tracuser_landing_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comments', models.TextField()),
            ],
            options={
                'verbose_name': 'User Landing Signup',
                'abstract': False,
                'db_table': 'tracuser_landing',
            },
        ),
    ]
