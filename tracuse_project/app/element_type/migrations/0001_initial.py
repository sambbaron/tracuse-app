# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementDataType',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('entity_name', models.CharField(max_length=40, default='', db_index=True)),
                ('schema_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('readable_name', models.CharField(max_length=40, default='', blank=True, db_index=True, null=True)),
                ('readable_plural_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('short_definition', models.CharField(max_length=25, null=True, blank=True)),
                ('long_definition', models.CharField(max_length=100, null=True, blank=True)),
                ('example', models.CharField(max_length=100, null=True, blank=True)),
                ('element_data_type_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Element Data Type',
                'db_table': 'element_data_type',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementDatumObject',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('element_datum_object_id', models.AutoField(primary_key=True, serialize=False)),
                ('datum_object', models.ForeignKey(related_name='element_datum_objects', db_column='datum_object_id', to='datum.DatumObject')),
            ],
            options={
                'ordering': ['sort'],
                'verbose_name': 'Datum Object - Element',
                'db_table': 'element_datum_object',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementDatumType',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('entity_name', models.CharField(max_length=40, default='', db_index=True)),
                ('schema_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('readable_name', models.CharField(max_length=40, default='', blank=True, db_index=True, null=True)),
                ('readable_plural_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('short_definition', models.CharField(max_length=25, null=True, blank=True)),
                ('long_definition', models.CharField(max_length=100, null=True, blank=True)),
                ('example', models.CharField(max_length=100, null=True, blank=True)),
                ('element_datum_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('calc_expression', models.CharField(max_length=255, default='', blank=True)),
                ('primary_view', models.BooleanField(default=False)),
                ('datum_type', models.ForeignKey(related_name='element_datum_types', db_column='datum_type_id', to='datum.DatumType')),
            ],
            options={
                'ordering': ['sort'],
                'verbose_name': 'Datum Type - Element',
                'db_table': 'element_datum_type',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementOperator',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('entity_name', models.CharField(max_length=40, default='', db_index=True)),
                ('schema_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('readable_name', models.CharField(max_length=40, default='', blank=True, db_index=True, null=True)),
                ('readable_plural_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('short_definition', models.CharField(max_length=25, null=True, blank=True)),
                ('long_definition', models.CharField(max_length=100, null=True, blank=True)),
                ('example', models.CharField(max_length=100, null=True, blank=True)),
                ('element_operator_id', models.AutoField(primary_key=True, serialize=False)),
                ('default_operator', models.BooleanField(default=False)),
                ('element_data_type', models.ForeignKey(related_name='operators', db_column='element_data_type_id', to='element_type.ElementDataType')),
            ],
            options={
                'verbose_name': 'Element Data Type Operator',
                'db_table': 'element_operator',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementOption',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('entity_name', models.CharField(max_length=40, default='', db_index=True)),
                ('schema_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('readable_name', models.CharField(max_length=40, default='', blank=True, db_index=True, null=True)),
                ('readable_plural_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('short_definition', models.CharField(max_length=25, null=True, blank=True)),
                ('long_definition', models.CharField(max_length=100, null=True, blank=True)),
                ('example', models.CharField(max_length=100, null=True, blank=True)),
                ('element_option_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Element Option',
                'db_table': 'element_option',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementType',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('entity_name', models.CharField(max_length=40, default='', db_index=True)),
                ('schema_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('readable_name', models.CharField(max_length=40, default='', blank=True, db_index=True, null=True)),
                ('readable_plural_name', models.CharField(max_length=40, default='', blank=True, null=True)),
                ('short_definition', models.CharField(max_length=25, null=True, blank=True)),
                ('long_definition', models.CharField(max_length=100, null=True, blank=True)),
                ('example', models.CharField(max_length=100, null=True, blank=True)),
                ('element_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_expression', models.CharField(max_length=255, default='', blank=True)),
                ('editable', models.BooleanField()),
                ('element_view', models.CharField(max_length=25, default='ElementText')),
                ('datum_objects', models.ManyToManyField(related_name='+', to='datum.DatumObject', through='element_type.ElementDatumObject')),
                ('datum_types', models.ManyToManyField(related_name='+', to='datum.DatumType', through='element_type.ElementDatumType')),
                ('element_data_type', models.ForeignKey(related_name='element_types', db_column='element_data_type_id', to='element_type.ElementDataType')),
            ],
            options={
                'db_table': 'element_type',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='elementoption',
            name='element_type',
            field=models.ForeignKey(related_name='element_options', db_column='element_type_id', to='element_type.ElementType'),
        ),
        migrations.AddField(
            model_name='elementdatumtype',
            name='element_type',
            field=models.ForeignKey(related_name='datum_element_types', db_column='element_type_id', to='element_type.ElementType'),
        ),
        migrations.AddField(
            model_name='elementdatumobject',
            name='element_type',
            field=models.ForeignKey(related_name='datum_object_elements', db_column='element_type_id', to='element_type.ElementType'),
        ),
        migrations.AlterUniqueTogether(
            name='elementdatumtype',
            unique_together=set([('datum_type', 'element_type')]),
        ),
        migrations.AlterIndexTogether(
            name='elementdatumtype',
            index_together=set([('datum_type', 'element_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='elementdatumobject',
            unique_together=set([('datum_object', 'element_type')]),
        ),
        migrations.AlterIndexTogether(
            name='elementdatumobject',
            index_together=set([('datum_object', 'element_type')]),
        ),
    ]
