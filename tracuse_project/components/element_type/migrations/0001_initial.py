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
                ('short_definition', models.CharField(null=True, max_length=25, blank=True)),
                ('long_definition', models.CharField(null=True, max_length=100, blank=True)),
                ('element_data_type_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Element Data Type',
                'db_table': 'element_data_type',
            },
        ),
        migrations.CreateModel(
            name='ElementOption',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, max_length=25, blank=True)),
                ('long_definition', models.CharField(null=True, max_length=100, blank=True)),
                ('element_option_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Element Option',
                'db_table': 'element_option',
            },
        ),
        migrations.CreateModel(
            name='ElementType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, max_length=25, blank=True)),
                ('long_definition', models.CharField(null=True, max_length=100, blank=True)),
                ('element_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('default_expression', models.CharField(null=True, max_length=255, blank=True)),
                ('editable', models.BooleanField()),
                ('element_data_type', models.ForeignKey(db_column='element_data_type_id', related_name='element_types', to='element_type.ElementDataType')),
            ],
            options={
                'abstract': False,
                'db_table': 'element_type',
            },
        ),
        migrations.CreateModel(
            name='ElementTypeDatumObject',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('element_type_datum_object_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_object', models.ForeignKey(db_column='datum_object_id', related_name='element_types_datum_objects', to='datum.DatumObject')),
                ('element_type', models.ForeignKey(db_column='element_type_id', related_name='datum_objects_element_types', to='element_type.ElementType')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Element Type - Datum Object',
                'db_table': 'element_type_datum_object',
            },
        ),
        migrations.CreateModel(
            name='ElementTypeDatumType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('element_type_datum_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_type', models.ForeignKey(db_column='datum_type_id', related_name='element_types_datum_types', to='datum.DatumType')),
                ('element_type', models.ForeignKey(db_column='element_type_id', related_name='datum_types_element_types', to='element_type.ElementType')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Element Type - Datum Type',
                'db_table': 'element_type_datum_type',
            },
        ),
        migrations.AddField(
            model_name='elementoption',
            name='element_type',
            field=models.ForeignKey(db_column='element_type_id', related_name='element_options', to='element_type.ElementType'),
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
