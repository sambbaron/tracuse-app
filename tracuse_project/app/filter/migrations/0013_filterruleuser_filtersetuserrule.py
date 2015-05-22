# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filter', '0012_filterrule_operator_default_exact'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterRuleUser',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('operator', models.CharField(max_length=5, choices=[('exact', 'equals'), ('Text', (('iexact', 'text equals'), ('icontains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))], default='exact')),
                ('conditional', models.CharField(null=True, blank=True, max_length=3, choices=[('AND', 'AND'), ('OR', 'OR')], default='AND')),
                ('filter_rule_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(related_name='filter_rule_users', db_column='user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['sort'],
                'verbose_name': 'Filter Rule - User',
                'db_table': 'filter_rule_user',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FilterSetUserRule',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('filter_set_user_rule_id', models.AutoField(primary_key=True, serialize=False)),
                ('filter_rule_user', models.ForeignKey(related_name='filter_set_user_rules', db_column='filter_rule_user_id', to='filter.FilterRuleUser')),
                ('filter_set', models.ForeignKey(related_name='filter_set_user_rules', db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'ordering': ['sort'],
                'db_table': 'filter_set_user_rule',
                'abstract': False,
            },
        ),
    ]
