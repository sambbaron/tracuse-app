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
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('element_data_type_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'element_data_type',
                'abstract': False,
                'verbose_name': 'Element Data Type',
            },
        ),
        migrations.CreateModel(
            name='ElementOption',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('element_option_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'element_option',
                'abstract': False,
                'verbose_name': 'Element Option',
            },
        ),
        migrations.CreateModel(
            name='ElementType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('element_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('default_expression', models.CharField(null=True, blank=True, max_length=255)),
                ('editable', models.BooleanField()),
                ('element_data_type', models.ForeignKey(related_name='element_types', db_column='element_data_type_id', to='element_type.ElementDataType')),
            ],
            options={
                'db_table': 'element_type',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementTypeDatumObject',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('element_type_datum_object_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_object', models.ForeignKey(related_name='element_types_datum_objects', db_column='datum_object_id', to='datum.DatumObject')),
                ('element_type', models.ForeignKey(related_name='datum_objects_element_types', db_column='element_type_id', to='element_type.ElementType')),
            ],
            options={
                'db_table': 'element_type_datum_object',
                'abstract': False,
                'verbose_name': 'Element Type - Datum Object',
            },
        ),
        migrations.CreateModel(
            name='ElementTypeDatumType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('element_type_datum_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_type', models.ForeignKey(related_name='element_types_datum_types', db_column='datum_type_id', to='datum.DatumType')),
                ('element_type', models.ForeignKey(related_name='datum_types_element_types', db_column='element_type_id', to='element_type.ElementType')),
            ],
            options={
                'db_table': 'element_type_datum_type',
                'abstract': False,
                'verbose_name': 'Element Type - Datum Type',
            },
        ),
        migrations.AddField(
            model_name='elementoption',
            name='element_type',
            field=models.ForeignKey(related_name='element_options', db_column='element_type_id', to='element_type.ElementType'),
        ),
        migrations.AlterUniqueTogether(
            name='elementtypedatumtype',
            unique_together=set([('datum_type', 'element_type')]),
        ),
        migrations.AlterIndexTogether(
            name='elementtypedatumtype',
            index_together=set([('datum_type', 'element_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='elementtypedatumobject',
            unique_together=set([('datum_object', 'element_type')]),
        ),
        migrations.AlterIndexTogether(
            name='elementtypedatumobject',
            index_together=set([('datum_object', 'element_type')]),
        ),
    ]
