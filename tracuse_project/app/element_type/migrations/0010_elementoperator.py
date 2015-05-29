# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0009_entitymixin_increase_name_len'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementOperator',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('entity_name', models.CharField(db_index=True, max_length=40, default='')),
                ('schema_name', models.CharField(max_length=40, default='')),
                ('readable_name', models.CharField(db_index=True, max_length=40, default='')),
                ('readable_plural_name', models.CharField(max_length=40, default='')),
                ('short_definition', models.CharField(blank=True, null=True, max_length=25)),
                ('long_definition', models.CharField(blank=True, null=True, max_length=100)),
                ('example', models.CharField(blank=True, null=True, max_length=100)),
                ('element_operator_id', models.AutoField(serialize=False, primary_key=True)),
                ('default_operator', models.BooleanField(default=False)),
                ('element_data_type', models.ForeignKey(db_column='element_data_type_id', related_name='operators', to='element_type.ElementDataType')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Element Data Type Operators',
                'db_table': 'element_operator',
            },
        ),
    ]
