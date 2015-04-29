# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('association', '0001_initial'),
        ('datum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterRuleAssociation',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('operator', models.CharField(default='=', max_length=5)),
                ('conditional', models.CharField(null=True, blank=True, max_length=3, choices=[('AND', 'AND'), ('OR', 'OR')])),
                ('filter_rule_association_id', models.AutoField(serialize=False, primary_key=True)),
                ('depth', models.IntegerField(default=1)),
                ('association_direction', models.ForeignKey(related_name='filter_rule_associations', db_column='association_direction_id', to='association.AssociationDirection')),
                ('association_type_id', models.ForeignKey(related_name='filter_rule_associations', db_column='association_type_id', to='association.AssociationType')),
                ('datum_object', models.ForeignKey(related_name='filter_rule_associations', db_column='datum_object_id', to='datum.DatumObject')),
            ],
            options={
                'db_table': 'filter_rule_association',
                'abstract': False,
                'verbose_name': 'Filter Rule - Association',
            },
        ),
        migrations.CreateModel(
            name='FilterRuleElement',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('operator', models.CharField(default='=', max_length=5)),
                ('conditional', models.CharField(null=True, blank=True, max_length=3, choices=[('AND', 'AND'), ('OR', 'OR')])),
                ('filter_rule_element_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.CharField(max_length=255)),
                ('element_type', models.ForeignKey(related_name='filter_rule_elements', db_column='element_type_id', to='element_type.ElementType')),
            ],
            options={
                'db_table': 'filter_rule_element',
                'abstract': False,
                'verbose_name': 'Filter Rule - Element',
            },
        ),
        migrations.CreateModel(
            name='FilterRuleGroup',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('operator', models.CharField(default='=', max_length=5)),
                ('conditional', models.CharField(null=True, blank=True, max_length=3, choices=[('AND', 'AND'), ('OR', 'OR')])),
                ('filter_rule_group_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_group', models.ForeignKey(related_name='filter_rule_groups', db_column='datum_group_id', to='datum.DatumGroup')),
            ],
            options={
                'db_table': 'filter_rule_group',
                'abstract': False,
                'verbose_name': 'Filter Rule - Group',
            },
        ),
        migrations.CreateModel(
            name='FilterRuleType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('operator', models.CharField(default='=', max_length=5)),
                ('conditional', models.CharField(null=True, blank=True, max_length=3, choices=[('AND', 'AND'), ('OR', 'OR')])),
                ('filter_rule_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_type', models.ForeignKey(related_name='filter_rule_types', db_column='datum_type_id', to='datum.DatumType')),
            ],
            options={
                'db_table': 'filter_rule_type',
                'abstract': False,
                'verbose_name': 'Filter Rule - Type',
            },
        ),
        migrations.CreateModel(
            name='FilterSet',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('filter_set_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.ForeignKey(null=True, blank=True, related_name='filter_sets', db_column='user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'filter_set',
                'abstract': False,
                'verbose_name': 'Filter Set',
            },
        ),
        migrations.CreateModel(
            name='FilterSetAssociationRule',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('filter_set_association_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_association_id', models.ForeignKey(to='filter.FilterRuleAssociation', db_column='filter_rule_association_id')),
                ('filter_set_id', models.ForeignKey(to='filter.FilterSet', db_column='filter_set_id')),
            ],
            options={
                'default_related_name': 'filter_set_association_rules',
                'db_table': 'filter_set_association_rule',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FilterSetElementRule',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('filter_set_element_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_element_id', models.ForeignKey(to='filter.FilterRuleElement', db_column='filter_rule_element_id')),
                ('filter_set_id', models.ForeignKey(to='filter.FilterSet', db_column='filter_set_id')),
            ],
            options={
                'default_related_name': 'filter_set_element_rules',
                'db_table': 'filter_set_element_rule',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FilterSetGroupRule',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('filter_set_group_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_group_id', models.ForeignKey(to='filter.FilterRuleGroup', db_column='filter_rule_group_id')),
                ('filter_set_id', models.ForeignKey(to='filter.FilterSet', db_column='filter_set_id')),
            ],
            options={
                'default_related_name': 'filter_set_group_rules',
                'db_table': 'filter_set_group_rule',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FilterSetTypeRule',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('filter_set_type_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_type_id', models.ForeignKey(to='filter.FilterRuleType', db_column='filter_rule_type_id')),
                ('filter_set_id', models.ForeignKey(to='filter.FilterSet', db_column='filter_set_id')),
            ],
            options={
                'default_related_name': 'filter_set_type_rules',
                'db_table': 'filter_set_type_rule',
                'abstract': False,
            },
        ),
    ]
