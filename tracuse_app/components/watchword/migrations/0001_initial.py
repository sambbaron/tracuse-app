# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0001_initial'),
        ('filter', '0001_initial'),
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
                ('association_type', models.ForeignKey(db_column='association_type_id', to='association.AssociationType')),
                ('filter_test_scope', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet', null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Association Type Watchword',
                'db_table': 'watchword_association_type',
            },
        ),
        migrations.CreateModel(
            name='WatchwordDatumObject',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('watchword', models.CharField(max_length=100)),
                ('watchword_datum_object_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_object', models.ForeignKey(db_column='datum_object_id', to='datum.DatumObject')),
                ('filter_test_scope', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet', null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Datum Object Watchword',
                'db_table': 'watchword_datum_object',
            },
        ),
        migrations.CreateModel(
            name='WatchwordDatumType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('watchword', models.CharField(max_length=100)),
                ('watchword_datum_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_type', models.ForeignKey(db_column='datum_type_id', to='datum.DatumType')),
                ('filter_test_scope', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet', null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Datum Type Watchword',
                'db_table': 'watchword_datum_type',
            },
        ),
    ]
