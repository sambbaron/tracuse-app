# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementValueBinary',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('element_value_binary_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.BinaryField(blank=True, null=True)),
                ('element_datum_object', models.OneToOneField(to='element_type.ElementDatumObject', db_column='element_datum_object_id')),
                ('element_option', models.ForeignKey(to='element_type.ElementOption', null=True, db_column='element_option_id', blank=True)),
            ],
            options={
                'db_table': 'element_value_binary',
                'verbose_name': 'Element Value',
                'abstract': False,
                'default_related_name': 'element_value_binary',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='ElementValueBoolean',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('element_value_boolean_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.BooleanField()),
                ('element_datum_object', models.OneToOneField(to='element_type.ElementDatumObject', db_column='element_datum_object_id')),
                ('element_option', models.ForeignKey(to='element_type.ElementOption', null=True, db_column='element_option_id', blank=True)),
            ],
            options={
                'db_table': 'element_value_boolean',
                'verbose_name': 'Element Value',
                'abstract': False,
                'default_related_name': 'element_value_boolean',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='ElementValueDatetime',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('element_value_datetime_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.DateTimeField(blank=True, null=True)),
                ('element_datum_object', models.OneToOneField(to='element_type.ElementDatumObject', db_column='element_datum_object_id')),
                ('element_option', models.ForeignKey(to='element_type.ElementOption', null=True, db_column='element_option_id', blank=True)),
            ],
            options={
                'db_table': 'element_value_datetime',
                'verbose_name': 'Element Value',
                'abstract': False,
                'default_related_name': 'element_value_datetime',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='ElementValueDecimal',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('element_value_decimal_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)),
                ('element_datum_object', models.OneToOneField(to='element_type.ElementDatumObject', db_column='element_datum_object_id')),
                ('element_option', models.ForeignKey(to='element_type.ElementOption', null=True, db_column='element_option_id', blank=True)),
            ],
            options={
                'db_table': 'element_value_decimal',
                'verbose_name': 'Element Value',
                'abstract': False,
                'default_related_name': 'element_value_decimal',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='ElementValueString',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('element_value_string_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.CharField(max_length=150, blank=True, default='')),
                ('element_datum_object', models.OneToOneField(to='element_type.ElementDatumObject', db_column='element_datum_object_id')),
                ('element_option', models.ForeignKey(to='element_type.ElementOption', null=True, db_column='element_option_id', blank=True)),
            ],
            options={
                'db_table': 'element_value_string',
                'verbose_name': 'Element Value',
                'abstract': False,
                'default_related_name': 'element_value_string',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='ElementValueTextData',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('element_value_textdata_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.TextField(blank=True, default='')),
                ('element_datum_object', models.OneToOneField(to='element_type.ElementDatumObject', db_column='element_datum_object_id')),
                ('element_option', models.ForeignKey(to='element_type.ElementOption', null=True, db_column='element_option_id', blank=True)),
            ],
            options={
                'db_table': 'element_value_textdata',
                'verbose_name': 'Element Value',
                'abstract': False,
                'default_related_name': 'element_value_textdata',
                'ordering': ['sort'],
            },
        ),
    ]
