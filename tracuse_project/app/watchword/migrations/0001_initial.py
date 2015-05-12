# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0001_initial'),
        ('association', '0001_initial'),
        ('filter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchwordAssociationType',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('watchword', models.CharField(max_length=100)),
                ('watchword_association_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('association_type', models.ForeignKey(db_column='association_type_id', to='association.AssociationType')),
                ('filter_test_scope', models.ForeignKey(to='filter.FilterSet', null=True, db_column='filter_set_id', blank=True)),
            ],
            options={
                'db_table': 'watchword_association_type',
                'verbose_name': 'Association Type Watchword',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='WatchwordDatumObject',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('watchword', models.CharField(max_length=100)),
                ('watchword_datum_object_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_object', models.ForeignKey(db_column='datum_object_id', to='datum.DatumObject')),
                ('filter_test_scope', models.ForeignKey(to='filter.FilterSet', null=True, db_column='filter_set_id', blank=True)),
            ],
            options={
                'db_table': 'watchword_datum_object',
                'verbose_name': 'Datum Object Watchword',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='WatchwordDatumType',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('watchword', models.CharField(max_length=100)),
                ('watchword_datum_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_type', models.ForeignKey(db_column='datum_type_id', to='datum.DatumType')),
                ('filter_test_scope', models.ForeignKey(to='filter.FilterSet', null=True, db_column='filter_set_id', blank=True)),
            ],
            options={
                'db_table': 'watchword_datum_type',
                'verbose_name': 'Datum Type Watchword',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
    ]
