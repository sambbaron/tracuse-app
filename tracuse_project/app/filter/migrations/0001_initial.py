# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datum', '0001_initial'),
        ('association', '0001_initial'),
        ('element_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterRuleAssociation',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('operator', models.CharField(max_length=25, default='exact', choices=[('exact', 'equals'), ('Text', (('iexact', 'text equals'), ('icontains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))])),
                ('conditional', models.CharField(max_length=3, default='AND', blank=True, choices=[('AND', 'AND'), ('OR', 'OR')], null=True)),
                ('filter_rule_association_id', models.AutoField(primary_key=True, serialize=False)),
                ('distance', models.IntegerField(default=1)),
                ('association_direction', models.ForeignKey(related_name='filter_rule_associations', db_column='association_direction_id', to='association.AssociationDirection')),
                ('association_type_id', models.ForeignKey(related_name='filter_rule_associations', db_column='association_type_id', to='association.AssociationType')),
                ('datum_object', models.ForeignKey(related_name='filter_rule_associations', db_column='datum_object_id', to='datum.DatumObject')),
            ],
            options={
                'verbose_name': 'Filter Rule - Association',
                'db_table': 'filter_rule_association',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterRuleDataType',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('operator', models.CharField(max_length=25, default='exact', choices=[('exact', 'equals'), ('Text', (('iexact', 'text equals'), ('icontains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))])),
                ('conditional', models.CharField(max_length=3, default='AND', blank=True, choices=[('AND', 'AND'), ('OR', 'OR')], null=True)),
                ('filter_rule_data_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('elvalue', models.CharField(max_length=255)),
                ('element_data_type', models.ForeignKey(related_name='filter_rule_data_types', db_column='element_data_type_id', to='element_type.ElementDataType')),
            ],
            options={
                'verbose_name': 'Filter Rule - Element Data Type',
                'db_table': 'filter_rule_data_type',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterRuleElement',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('operator', models.CharField(max_length=25, default='exact', choices=[('exact', 'equals'), ('Text', (('iexact', 'text equals'), ('icontains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))])),
                ('conditional', models.CharField(max_length=3, default='AND', blank=True, choices=[('AND', 'AND'), ('OR', 'OR')], null=True)),
                ('filter_rule_element_id', models.AutoField(primary_key=True, serialize=False)),
                ('elvalue', models.CharField(max_length=255)),
                ('element_type', models.ForeignKey(related_name='filter_rule_elements', db_column='element_type_id', to='element_type.ElementType')),
            ],
            options={
                'verbose_name': 'Filter Rule - Element',
                'db_table': 'filter_rule_element',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterRuleGroup',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('operator', models.CharField(max_length=25, default='exact', choices=[('exact', 'equals'), ('Text', (('iexact', 'text equals'), ('icontains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))])),
                ('conditional', models.CharField(max_length=3, default='AND', blank=True, choices=[('AND', 'AND'), ('OR', 'OR')], null=True)),
                ('filter_rule_group_id', models.AutoField(primary_key=True, serialize=False)),
                ('datum_group', models.ForeignKey(related_name='filter_rule_groups', db_column='datum_group_id', to='datum.DatumGroup')),
            ],
            options={
                'verbose_name': 'Filter Rule - Group',
                'db_table': 'filter_rule_group',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterRuleType',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('operator', models.CharField(max_length=25, default='exact', choices=[('exact', 'equals'), ('Text', (('iexact', 'text equals'), ('icontains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))])),
                ('conditional', models.CharField(max_length=3, default='AND', blank=True, choices=[('AND', 'AND'), ('OR', 'OR')], null=True)),
                ('filter_rule_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('datum_type', models.ForeignKey(related_name='filter_rule_types', db_column='datum_type_id', to='datum.DatumType')),
            ],
            options={
                'verbose_name': 'Filter Rule - Type',
                'db_table': 'filter_rule_type',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterRuleUser',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('operator', models.CharField(max_length=25, default='exact', choices=[('exact', 'equals'), ('Text', (('iexact', 'text equals'), ('icontains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))])),
                ('conditional', models.CharField(max_length=3, default='AND', blank=True, choices=[('AND', 'AND'), ('OR', 'OR')], null=True)),
                ('filter_rule_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(related_name='filter_rule_users', db_column='user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Filter Rule - User',
                'db_table': 'filter_rule_user',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterSet',
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
                ('filter_set_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Filter Set',
                'db_table': 'filter_set',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FilterSetAssociationRule',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('filter_set_association_rule_id', models.AutoField(primary_key=True, serialize=False)),
                ('filter_rule_association', models.ForeignKey(related_name='filter_set_association_rules', db_column='filter_rule_association_id', to='filter.FilterRuleAssociation')),
                ('filter_set', models.ForeignKey(related_name='filter_set_association_rules', db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'filter_set_association_rule',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterSetDataTypeRule',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('filter_set_data_type_rule_id', models.AutoField(primary_key=True, serialize=False)),
                ('filter_rule_data_type', models.ForeignKey(related_name='filter_set_data_type_rules', db_column='filter_rule_data_type_id', to='filter.FilterRuleDataType')),
                ('filter_set', models.ForeignKey(related_name='filter_set_data_type_rules', db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'filter_set_data_type_rule',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterSetElementRule',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('filter_set_element_rule_id', models.AutoField(primary_key=True, serialize=False)),
                ('filter_rule_element', models.ForeignKey(related_name='filter_set_element_rules', db_column='filter_rule_element_id', to='filter.FilterRuleElement')),
                ('filter_set', models.ForeignKey(related_name='filter_set_element_rules', db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'filter_set_element_rule',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterSetGroupRule',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('filter_set_group_rule_id', models.AutoField(primary_key=True, serialize=False)),
                ('filter_rule_group', models.ForeignKey(related_name='filter_set_group_rules', db_column='filter_rule_group_id', to='filter.FilterRuleGroup')),
                ('filter_set', models.ForeignKey(related_name='filter_set_group_rules', db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'filter_set_group_rule',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterSetTypeRule',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('filter_set_type_rule_id', models.AutoField(primary_key=True, serialize=False)),
                ('filter_rule_type', models.ForeignKey(related_name='filter_set_type_rules', db_column='filter_rule_type_id', to='filter.FilterRuleType')),
                ('filter_set', models.ForeignKey(related_name='filter_set_type_rules', db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'filter_set_type_rule',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterSetUserRule',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('filter_set_user_rule_id', models.AutoField(primary_key=True, serialize=False)),
                ('filter_rule_user', models.ForeignKey(related_name='filter_set_user_rules', db_column='filter_rule_user_id', to='filter.FilterRuleUser')),
                ('filter_set', models.ForeignKey(related_name='filter_set_user_rules', db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'filter_set_user_rule',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.AddField(
            model_name='filterset',
            name='filter_rules_association',
            field=models.ManyToManyField(related_name='+', to='filter.FilterRuleAssociation', through='filter.FilterSetAssociationRule'),
        ),
        migrations.AddField(
            model_name='filterset',
            name='filter_rules_data_type',
            field=models.ManyToManyField(related_name='+', to='filter.FilterRuleDataType', through='filter.FilterSetDataTypeRule'),
        ),
        migrations.AddField(
            model_name='filterset',
            name='filter_rules_element',
            field=models.ManyToManyField(related_name='+', to='filter.FilterRuleElement', through='filter.FilterSetElementRule'),
        ),
        migrations.AddField(
            model_name='filterset',
            name='filter_rules_group',
            field=models.ManyToManyField(related_name='+', to='filter.FilterRuleGroup', through='filter.FilterSetGroupRule'),
        ),
        migrations.AddField(
            model_name='filterset',
            name='filter_rules_type',
            field=models.ManyToManyField(related_name='+', to='filter.FilterRuleType', through='filter.FilterSetTypeRule'),
        ),
        migrations.AddField(
            model_name='filterset',
            name='filter_rules_user',
            field=models.ManyToManyField(related_name='+', to='filter.FilterRuleUser', through='filter.FilterSetUserRule'),
        ),
        migrations.AddField(
            model_name='filterset',
            name='user',
            field=models.ForeignKey(related_name='filter_sets', blank=True, null=True, db_column='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
