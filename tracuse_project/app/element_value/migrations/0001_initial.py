# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementValueBinary',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('element_value_binary_id', models.AutoField(primary_key=True, serialize=False)),
                ('elvalue', models.BinaryField(null=True, blank=True)),
                ('element_datum_object', models.OneToOneField(db_column='element_datum_object_id', to='element_type.ElementDatumObject')),
                ('element_option', models.ForeignKey(blank=True, null=True, db_column='element_option_id', to='element_type.ElementOption')),
            ],
            options={
                'verbose_name': 'Element Value',
                'db_table': 'element_value_binary',
                'abstract': False,
                'default_related_name': 'element_value_binary',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='ElementValueBoolean',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('element_value_boolean_id', models.AutoField(primary_key=True, serialize=False)),
                ('elvalue', models.BooleanField(default=False)),
                ('element_datum_object', models.OneToOneField(db_column='element_datum_object_id', to='element_type.ElementDatumObject')),
                ('element_option', models.ForeignKey(blank=True, null=True, db_column='element_option_id', to='element_type.ElementOption')),
            ],
            options={
                'verbose_name': 'Element Value',
                'db_table': 'element_value_boolean',
                'abstract': False,
                'default_related_name': 'element_value_boolean',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='ElementValueDatetime',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('element_value_datetime_id', models.AutoField(primary_key=True, serialize=False)),
                ('elvalue', models.DateTimeField(null=True, blank=True)),
                ('element_datum_object', models.OneToOneField(db_column='element_datum_object_id', to='element_type.ElementDatumObject')),
                ('element_option', models.ForeignKey(blank=True, null=True, db_column='element_option_id', to='element_type.ElementOption')),
            ],
            options={
                'verbose_name': 'Element Value',
                'db_table': 'element_value_datetime',
                'abstract': False,
                'default_related_name': 'element_value_datetime',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='ElementValueDecimal',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('element_value_decimal_id', models.AutoField(primary_key=True, serialize=False)),
                ('elvalue', models.DecimalField(decimal_places=2, null=True, default=0, blank=True, max_digits=10)),
                ('element_datum_object', models.OneToOneField(db_column='element_datum_object_id', to='element_type.ElementDatumObject')),
                ('element_option', models.ForeignKey(blank=True, null=True, db_column='element_option_id', to='element_type.ElementOption')),
            ],
            options={
                'verbose_name': 'Element Value',
                'db_table': 'element_value_decimal',
                'abstract': False,
                'default_related_name': 'element_value_decimal',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='ElementValueString',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('element_value_string_id', models.AutoField(primary_key=True, serialize=False)),
                ('elvalue', models.CharField(max_length=150, default='', blank=True)),
                ('element_datum_object', models.OneToOneField(db_column='element_datum_object_id', to='element_type.ElementDatumObject')),
                ('element_option', models.ForeignKey(blank=True, null=True, db_column='element_option_id', to='element_type.ElementOption')),
            ],
            options={
                'verbose_name': 'Element Value',
                'db_table': 'element_value_string',
                'abstract': False,
                'default_related_name': 'element_value_string',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='ElementValueTextData',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('element_value_textdata_id', models.AutoField(primary_key=True, serialize=False)),
                ('elvalue', models.TextField(default='', blank=True)),
                ('element_datum_object', models.OneToOneField(db_column='element_datum_object_id', to='element_type.ElementDatumObject')),
                ('element_option', models.ForeignKey(blank=True, null=True, db_column='element_option_id', to='element_type.ElementOption')),
            ],
            options={
                'verbose_name': 'Element Value',
                'db_table': 'element_value_textdata',
                'abstract': False,
                'default_related_name': 'element_value_textdata',
                'ordering': ['sort'],
            },
        ),
    ]
