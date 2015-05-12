# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
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
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('operator', models.CharField(max_length=5, default='=')),
                ('conditional', models.CharField(max_length=3, choices=[('AND', 'AND'), ('OR', 'OR')], blank=True, null=True)),
                ('filter_rule_association_id', models.AutoField(serialize=False, primary_key=True)),
                ('distance', models.IntegerField(default=1)),
                ('association_direction', models.ForeignKey(related_name='filter_rule_associations', to='association.AssociationDirection', db_column='association_direction_id')),
                ('association_type_id', models.ForeignKey(related_name='filter_rule_associations', to='association.AssociationType', db_column='association_type_id')),
                ('datum_object', models.ForeignKey(related_name='filter_rule_associations', to='datum.DatumObject', db_column='datum_object_id')),
            ],
            options={
                'db_table': 'filter_rule_association',
                'verbose_name': 'Filter Rule - Association',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterRuleElement',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('operator', models.CharField(max_length=5, default='=')),
                ('conditional', models.CharField(max_length=3, choices=[('AND', 'AND'), ('OR', 'OR')], blank=True, null=True)),
                ('filter_rule_element_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.CharField(max_length=255)),
                ('element_type', models.ForeignKey(related_name='filter_rule_elements', to='element_type.ElementType', db_column='element_type_id')),
            ],
            options={
                'db_table': 'filter_rule_element',
                'verbose_name': 'Filter Rule - Element',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterRuleGroup',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('operator', models.CharField(max_length=5, default='=')),
                ('conditional', models.CharField(max_length=3, choices=[('AND', 'AND'), ('OR', 'OR')], blank=True, null=True)),
                ('filter_rule_group_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_group', models.ForeignKey(related_name='filter_rule_groups', to='datum.DatumGroup', db_column='datum_group_id')),
            ],
            options={
                'db_table': 'filter_rule_group',
                'verbose_name': 'Filter Rule - Group',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterRuleType',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('operator', models.CharField(max_length=5, default='=')),
                ('conditional', models.CharField(max_length=3, choices=[('AND', 'AND'), ('OR', 'OR')], blank=True, null=True)),
                ('filter_rule_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_type', models.ForeignKey(related_name='filter_rule_types', to='datum.DatumType', db_column='datum_type_id')),
            ],
            options={
                'db_table': 'filter_rule_type',
                'verbose_name': 'Filter Rule - Type',
                'abstract': False,
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterSet',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('entity_name', models.CharField(max_length=25, db_index=True, default='')),
                ('readable_name', models.CharField(max_length=25, db_index=True, default='')),
                ('schema_name', models.CharField(max_length=25, default='')),
                ('readable_plural_name', models.CharField(max_length=25, default='')),
                ('short_definition', models.CharField(max_length=25, blank=True, null=True)),
                ('long_definition', models.CharField(max_length=100, blank=True, null=True)),
                ('filter_set_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.ForeignKey(related_name='filter_sets', to=settings.AUTH_USER_MODEL, null=True, db_column='user_id', blank=True)),
            ],
            options={
                'db_table': 'filter_set',
                'verbose_name': 'Filter Set',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FilterSetAssociationRule',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('filter_set_association_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_association_id', models.ForeignKey(db_column='filter_rule_association_id', to='filter.FilterRuleAssociation')),
                ('filter_set_id', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'filter_set_association_rule',
                'abstract': False,
                'default_related_name': 'filter_set_association_rules',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterSetElementRule',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('filter_set_element_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_element_id', models.ForeignKey(db_column='filter_rule_element_id', to='filter.FilterRuleElement')),
                ('filter_set_id', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'filter_set_element_rule',
                'abstract': False,
                'default_related_name': 'filter_set_element_rules',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterSetGroupRule',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('filter_set_group_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_group_id', models.ForeignKey(db_column='filter_rule_group_id', to='filter.FilterRuleGroup')),
                ('filter_set_id', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'filter_set_group_rule',
                'abstract': False,
                'default_related_name': 'filter_set_group_rules',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='FilterSetTypeRule',
            fields=[
                ('active', models.BooleanField(db_index=True, default=True)),
                ('sort', models.BigIntegerField(db_index=True, default=0)),
                ('filter_set_type_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_type_id', models.ForeignKey(db_column='filter_rule_type_id', to='filter.FilterRuleType')),
                ('filter_set_id', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'db_table': 'filter_set_type_rule',
                'abstract': False,
                'default_related_name': 'filter_set_type_rules',
                'ordering': ['sort'],
            },
        ),
    ]
