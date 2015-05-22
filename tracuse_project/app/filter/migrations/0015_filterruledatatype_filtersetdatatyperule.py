# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0009_entitymixin_increase_name_len'),
        ('filter', '0014_filterrule_operator_maxlength'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterRuleDataType',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('operator', models.CharField(default='exact', max_length=25, choices=[('exact', 'equals'), ('Text', (('iexact', 'text equals'), ('icontains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))])),
                ('conditional', models.CharField(blank=True, null=True, default='AND', max_length=3, choices=[('AND', 'AND'), ('OR', 'OR')])),
                ('filter_rule_data_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('elvalue', models.CharField(max_length=255)),
                ('element_data_type', models.ForeignKey(related_name='filter_rule_data_types', to='element_type.ElementDataType', db_column='element_data_type_id')),
            ],
            options={
                'ordering': ['sort'],
                'db_table': 'filter_rule_data_type',
                'abstract': False,
                'verbose_name': 'Filter Rule - Element Data Type',
            },
        ),
        migrations.CreateModel(
            name='FilterSetDataTypeRule',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('filter_set_data_type_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_data_type', models.ForeignKey(related_name='filter_set_data_type_rules', to='filter.FilterRuleDataType', db_column='filter_rule_data_type_id')),
                ('filter_set', models.ForeignKey(related_name='filter_set_data_type_rules', to='filter.FilterSet', db_column='filter_set_id')),
            ],
            options={
                'ordering': ['sort'],
                'db_table': 'filter_set_data_type_rule',
                'abstract': False,
            },
        ),
    ]
