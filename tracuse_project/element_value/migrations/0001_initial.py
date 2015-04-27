# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0004_elementtypedatumobject'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementValueBinary',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('element_value_binary_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.BinaryField()),
                ('element_option', models.ForeignKey(db_column='element_option_id', to='element_type.ElementOption')),
                ('element_type_datum_object', models.OneToOneField(to='element_type.ElementTypeDatumObject', db_column='element_type_datum_object_id')),
            ],
            options={
                'abstract': False,
                'db_table': 'element_value_binary',
            },
        ),
        migrations.CreateModel(
            name='ElementValueBoolean',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('element_value_boolean_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.BooleanField()),
                ('element_option', models.ForeignKey(db_column='element_option_id', to='element_type.ElementOption')),
                ('element_type_datum_object', models.OneToOneField(to='element_type.ElementTypeDatumObject', db_column='element_type_datum_object_id')),
            ],
            options={
                'abstract': False,
                'db_table': 'element_value_boolean',
            },
        ),
        migrations.CreateModel(
            name='ElementValueDatetime',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('element_value_datetime_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.DateTimeField()),
                ('element_option', models.ForeignKey(db_column='element_option_id', to='element_type.ElementOption')),
                ('element_type_datum_object', models.OneToOneField(to='element_type.ElementTypeDatumObject', db_column='element_type_datum_object_id')),
            ],
            options={
                'abstract': False,
                'db_table': 'element_value_datetime',
            },
        ),
        migrations.CreateModel(
            name='ElementValueDecimal',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('element_value_decimal_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('element_option', models.ForeignKey(db_column='element_option_id', to='element_type.ElementOption')),
                ('element_type_datum_object', models.OneToOneField(to='element_type.ElementTypeDatumObject', db_column='element_type_datum_object_id')),
            ],
            options={
                'abstract': False,
                'db_table': 'element_value_decimal',
            },
        ),
        migrations.CreateModel(
            name='ElementValueString',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('element_value_string_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.CharField(max_length=150)),
                ('element_option', models.ForeignKey(db_column='element_option_id', to='element_type.ElementOption')),
                ('element_type_datum_object', models.OneToOneField(to='element_type.ElementTypeDatumObject', db_column='element_type_datum_object_id')),
            ],
            options={
                'abstract': False,
                'db_table': 'element_value_string',
            },
        ),
        migrations.CreateModel(
            name='ElementValueTextData',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('element_value_textdata_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.TextField()),
                ('element_option', models.ForeignKey(db_column='element_option_id', to='element_type.ElementOption')),
                ('element_type_datum_object', models.OneToOneField(to='element_type.ElementTypeDatumObject', db_column='element_type_datum_object_id')),
            ],
            options={
                'abstract': False,
                'db_table': 'element_value_textdata',
            },
        ),
    ]
