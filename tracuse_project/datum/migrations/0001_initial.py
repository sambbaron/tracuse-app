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
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('entity_name', models.CharField(db_index=True, max_length=25, default='')),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('datum_group_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'datum_group',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DatumObject',
            fields=[
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('datum_object_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'datum_object',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DatumType',
            fields=[
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('entity_name', models.CharField(db_index=True, max_length=25, default='')),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('datum_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('repr_expression', models.CharField(max_length=255)),
                ('datum_group', models.ForeignKey(to='datum.DatumGroup', db_column='datum_group_id')),
            ],
            options={
                'db_table': 'datum_type',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='datumobject',
            name='datum_type',
            field=models.ForeignKey(to='datum.DatumType', db_column='datum_type_id'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column='user_id'),
        ),
    ]
