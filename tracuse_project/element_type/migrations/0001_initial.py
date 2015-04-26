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
                ('entity_name', models.CharField(default='', db_index=True, max_length=25)),
                ('short_definition', models.CharField(blank=True, null=True, max_length=25)),
                ('long_definition', models.CharField(blank=True, null=True, max_length=100)),
                ('element_data_type_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'element_data_type',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementOption',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', db_index=True, max_length=25)),
                ('short_definition', models.CharField(blank=True, null=True, max_length=25)),
                ('long_definition', models.CharField(blank=True, null=True, max_length=100)),
                ('element_option_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'element_option',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', db_index=True, max_length=25)),
                ('short_definition', models.CharField(blank=True, null=True, max_length=25)),
                ('long_definition', models.CharField(blank=True, null=True, max_length=100)),
                ('element_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('default_expression', models.CharField(blank=True, null=True, max_length=255)),
                ('editable', models.BooleanField()),
                ('element_data_type', models.ForeignKey(db_column='element_data_type_id', to='element_type.ElementDataType')),
            ],
            options={
                'db_table': 'element_type',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementTypeDatumType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', db_index=True, max_length=25)),
                ('short_definition', models.CharField(blank=True, null=True, max_length=25)),
                ('long_definition', models.CharField(blank=True, null=True, max_length=100)),
                ('element_type_datum_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('datum_type', models.ForeignKey(db_column='datum_type_id', to='datum.DatumType')),
                ('element_type', models.ForeignKey(db_column='element_type_id', to='element_type.ElementType')),
            ],
            options={
                'db_table': 'element_type_datum_type',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='elementoption',
            name='element_type',
            field=models.ForeignKey(db_column='element_type_id', to='element_type.ElementType'),
        ),
        migrations.AlterUniqueTogether(
            name='elementtypedatumtype',
            unique_together=set([('datum_type', 'element_type')]),
        ),
        migrations.AlterIndexTogether(
            name='elementtypedatumtype',
            index_together=set([('datum_type', 'element_type')]),
        ),
    ]
