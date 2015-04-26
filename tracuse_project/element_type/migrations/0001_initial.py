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
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('entity_name', models.CharField(db_index=True, max_length=25, default='')),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('element_data_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('html_tag', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'element_data_type',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementOption',
            fields=[
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('entity_name', models.CharField(db_index=True, max_length=25, default='')),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('element_option_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'element_option',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementType',
            fields=[
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('entity_name', models.CharField(db_index=True, max_length=25, default='')),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('element_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('default_expression', models.CharField(null=True, blank=True, max_length=255)),
                ('editable', models.BooleanField()),
                ('data_type', models.ForeignKey(to='element_type.ElementDataType', db_column='data_type_id')),
            ],
            options={
                'db_table': 'element_type',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementTypeDatumType',
            fields=[
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('entity_name', models.CharField(db_index=True, max_length=25, default='')),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('element_type_datum_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_type', models.ForeignKey(to='datum.DatumType', db_column='datum_type_id')),
                ('element_type', models.ForeignKey(to='element_type.ElementType', db_column='element_type_id')),
            ],
            options={
                'db_table': 'element_type_datum_type',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='elementoption',
            name='element_type',
            field=models.ForeignKey(to='element_type.ElementType', db_column='element_type_id'),
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
