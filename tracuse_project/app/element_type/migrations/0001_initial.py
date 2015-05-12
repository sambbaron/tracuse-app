# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementDataType',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('entity_name', models.CharField(max_length=25, db_index=True, default='')),
                ('readable_name', models.CharField(max_length=25, db_index=True, default='')),
                ('schema_name', models.CharField(max_length=25, default='')),
                ('readable_plural_name', models.CharField(max_length=25, default='')),
                ('short_definition', models.CharField(max_length=25, blank=True, null=True)),
                ('long_definition', models.CharField(max_length=100, blank=True, null=True)),
                ('element_data_type_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'element_data_type',
                'verbose_name': 'Element Data Type',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementDatumObject',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('element_datum_object_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_object', models.ForeignKey(related_name='element_datum_objects', to='datum.DatumObject', db_column='datum_object_id')),
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
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('element_datum_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_type', models.ForeignKey(related_name='element_datum_types', to='datum.DatumType', db_column='datum_type_id')),
            ],
            options={
                'ordering': ['sort'],
                'verbose_name': 'Datum Type - Element',
                'db_table': 'element_datum_type',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementOption',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('entity_name', models.CharField(max_length=25, db_index=True, default='')),
                ('readable_name', models.CharField(max_length=25, db_index=True, default='')),
                ('schema_name', models.CharField(max_length=25, default='')),
                ('readable_plural_name', models.CharField(max_length=25, default='')),
                ('short_definition', models.CharField(max_length=25, blank=True, null=True)),
                ('long_definition', models.CharField(max_length=100, blank=True, null=True)),
                ('element_option_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'element_option',
                'verbose_name': 'Element Option',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementType',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('entity_name', models.CharField(max_length=25, db_index=True, default='')),
                ('readable_name', models.CharField(max_length=25, db_index=True, default='')),
                ('schema_name', models.CharField(max_length=25, default='')),
                ('readable_plural_name', models.CharField(max_length=25, default='')),
                ('short_definition', models.CharField(max_length=25, blank=True, null=True)),
                ('long_definition', models.CharField(max_length=100, blank=True, null=True)),
                ('element_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('default_expression', models.CharField(max_length=255, blank=True, default='')),
                ('editable', models.BooleanField()),
                ('html_element', models.CharField(max_length=25, default='text')),
                ('datum_objects', models.ManyToManyField(related_name='+', to='datum.DatumObject', through='element_type.ElementDatumObject')),
                ('datum_types', models.ManyToManyField(related_name='+', to='datum.DatumType', through='element_type.ElementDatumType')),
                ('element_data_type', models.ForeignKey(related_name='element_types', to='element_type.ElementDataType', db_column='element_data_type_id')),
            ],
            options={
                'db_table': 'element_type',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='elementoption',
            name='element_type',
            field=models.ForeignKey(related_name='element_options', to='element_type.ElementType', db_column='element_type_id'),
        ),
        migrations.AddField(
            model_name='elementdatumtype',
            name='element_type',
            field=models.ForeignKey(related_name='datum_element_types', to='element_type.ElementType', db_column='element_type_id'),
        ),
        migrations.AddField(
            model_name='elementdatumobject',
            name='element_type',
            field=models.ForeignKey(related_name='datum_object_elements', to='element_type.ElementType', db_column='element_type_id'),
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
