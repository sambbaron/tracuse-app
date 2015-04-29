# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0005_meta_options'),
        ('association', '0005_meta_options'),
        ('filter', '0002_meta_options'),
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
                ('filter_test_scope', models.ForeignKey(blank=True, null=True, db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'watchword_association_type',
                'verbose_name': 'Association Type Watchword',
                'abstract': False,
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
                ('filter_test_scope', models.ForeignKey(blank=True, null=True, db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'watchword_datum_object',
                'verbose_name': 'Datum Object Watchword',
                'abstract': False,
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
                ('filter_test_scope', models.ForeignKey(blank=True, null=True, db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'watchword_datum_type',
                'verbose_name': 'Datum Type Watchword',
                'abstract': False,
            },
        ),
    ]
