# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0001_initial'),
        ('filter', '0001_initial'),
        ('association', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchwordAssociationType',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('watchword', models.CharField(max_length=100)),
                ('watchword_association_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('association_type', models.ForeignKey(db_column='association_type_id', to='association.AssociationType')),
                ('filter_test_scope', models.ForeignKey(blank=True, null=True, db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'verbose_name': 'Association Type Watchword',
                'db_table': 'watchword_association_type',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='WatchwordDatumObject',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('watchword', models.CharField(max_length=100)),
                ('watchword_datum_object_id', models.AutoField(primary_key=True, serialize=False)),
                ('datum_object', models.ForeignKey(db_column='datum_object_id', to='datum.DatumObject')),
                ('filter_test_scope', models.ForeignKey(blank=True, null=True, db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'verbose_name': 'Datum Object Watchword',
                'db_table': 'watchword_datum_object',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='WatchwordDatumType',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('watchword', models.CharField(max_length=100)),
                ('watchword_datum_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('datum_type', models.ForeignKey(db_column='datum_type_id', to='datum.DatumType')),
                ('filter_test_scope', models.ForeignKey(blank=True, null=True, db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'verbose_name': 'Datum Type Watchword',
                'db_table': 'watchword_datum_type',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
    ]
