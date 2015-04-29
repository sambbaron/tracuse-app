# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0001_initial'),
        ('association', '0001_initial'),
        ('datum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchwordAssociationType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('watchword', models.CharField(max_length=100)),
                ('watchword_association_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('association_type', models.ForeignKey(to='association.AssociationType', db_column='association_type_id')),
                ('filter_test_scope', models.ForeignKey(null=True, blank=True, db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'watchword_association_type',
                'abstract': False,
                'verbose_name': 'Association Type Watchword',
            },
        ),
        migrations.CreateModel(
            name='WatchwordDatumObject',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('watchword', models.CharField(max_length=100)),
                ('watchword_datum_object_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_object', models.ForeignKey(to='datum.DatumObject', db_column='datum_object_id')),
                ('filter_test_scope', models.ForeignKey(null=True, blank=True, db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'watchword_datum_object',
                'abstract': False,
                'verbose_name': 'Datum Object Watchword',
            },
        ),
        migrations.CreateModel(
            name='WatchwordDatumType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('watchword', models.CharField(max_length=100)),
                ('watchword_datum_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_type', models.ForeignKey(to='datum.DatumType', db_column='datum_type_id')),
                ('filter_test_scope', models.ForeignKey(null=True, blank=True, db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'watchword_datum_type',
                'abstract': False,
                'verbose_name': 'Datum Type Watchword',
            },
        ),
    ]
