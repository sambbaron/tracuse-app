# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatumGroup',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', db_index=True, max_length=25)),
                ('short_definition', models.CharField(blank=True, null=True, max_length=25)),
                ('long_definition', models.CharField(blank=True, null=True, max_length=100)),
                ('datum_group_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'datum_group',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DatumObject',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('datum_object_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'datum_object',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DatumType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', db_index=True, max_length=25)),
                ('short_definition', models.CharField(blank=True, null=True, max_length=25)),
                ('long_definition', models.CharField(blank=True, null=True, max_length=100)),
                ('datum_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('repr_expression', models.CharField(max_length=255)),
                ('datum_group', models.ForeignKey(db_column='datum_group_id', to='datum.DatumGroup')),
            ],
            options={
                'db_table': 'datum_type',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='datumobject',
            name='datum_type',
            field=models.ForeignKey(db_column='datum_type_id', to='datum.DatumType'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='user',
            field=models.ForeignKey(db_column='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
