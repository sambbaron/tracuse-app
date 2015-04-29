# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('element_type', '0001_initial'),
        ('datum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterRuleAssociation',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('operator', models.CharField(default='=', max_length=5)),
                ('conditional', models.CharField(null=True, choices=[('AND', 'AND'), ('OR', 'OR')], blank=True, max_length=3)),
                ('filter_rule_association_id', models.AutoField(serialize=False, primary_key=True)),
                ('depth', models.IntegerField(default=1)),
                ('association_direction', models.ForeignKey(db_column='association_direction_id', related_name='filter_rule_associations', to='association.AssociationDirection')),
                ('association_type_id', models.ForeignKey(db_column='association_type_id', related_name='filter_rule_associations', to='association.AssociationType')),
                ('datum_object', models.ForeignKey(db_column='datum_object_id', related_name='filter_rule_associations', to='datum.DatumObject')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Filter Rule - Association',
                'db_table': 'filter_rule_association',
            },
        ),
        migrations.CreateModel(
            name='FilterRuleElement',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('operator', models.CharField(default='=', max_length=5)),
                ('conditional', models.CharField(null=True, choices=[('AND', 'AND'), ('OR', 'OR')], blank=True, max_length=3)),
                ('filter_rule_element_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.CharField(max_length=255)),
                ('element_type', models.ForeignKey(db_column='element_type_id', related_name='filter_rule_elements', to='element_type.ElementType')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Filter Rule - Element',
                'db_table': 'filter_rule_element',
            },
        ),
        migrations.CreateModel(
            name='FilterRuleGroup',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('operator', models.CharField(default='=', max_length=5)),
                ('conditional', models.CharField(null=True, choices=[('AND', 'AND'), ('OR', 'OR')], blank=True, max_length=3)),
                ('filter_rule_group_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_group', models.ForeignKey(db_column='datum_group_id', related_name='filter_rule_groups', to='datum.DatumGroup')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Filter Rule - Group',
                'db_table': 'filter_rule_group',
            },
        ),
        migrations.CreateModel(
            name='FilterRuleType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('operator', models.CharField(default='=', max_length=5)),
                ('conditional', models.CharField(null=True, choices=[('AND', 'AND'), ('OR', 'OR')], blank=True, max_length=3)),
                ('filter_rule_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_type', models.ForeignKey(db_column='datum_type_id', related_name='filter_rule_types', to='datum.DatumType')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Filter Rule - Type',
                'db_table': 'filter_rule_type',
            },
        ),
        migrations.CreateModel(
            name='FilterSet',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, max_length=25, blank=True)),
                ('long_definition', models.CharField(null=True, max_length=100, blank=True)),
                ('filter_set_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.ForeignKey(db_column='user_id', to=settings.AUTH_USER_MODEL, null=True, related_name='filter_sets', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Filter Set',
                'db_table': 'filter_set',
            },
        ),
        migrations.CreateModel(
            name='FilterSetAssociationRule',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('filter_set_association_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_association_id', models.ForeignKey(db_column='filter_rule_association_id', to='filter.FilterRuleAssociation')),
                ('filter_set_id', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'abstract': False,
                'default_related_name': 'filter_set_association_rules',
                'db_table': 'filter_set_association_rule',
            },
        ),
        migrations.CreateModel(
            name='FilterSetElementRule',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('filter_set_element_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_element_id', models.ForeignKey(db_column='filter_rule_element_id', to='filter.FilterRuleElement')),
                ('filter_set_id', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'abstract': False,
                'default_related_name': 'filter_set_element_rules',
                'db_table': 'filter_set_element_rule',
            },
        ),
        migrations.CreateModel(
            name='FilterSetGroupRule',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('filter_set_group_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_group_id', models.ForeignKey(db_column='filter_rule_group_id', to='filter.FilterRuleGroup')),
                ('filter_set_id', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'abstract': False,
                'default_related_name': 'filter_set_group_rules',
                'db_table': 'filter_set_group_rule',
            },
        ),
        migrations.CreateModel(
            name='FilterSetTypeRule',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('filter_set_type_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_type_id', models.ForeignKey(db_column='filter_rule_type_id', to='filter.FilterRuleType')),
                ('filter_set_id', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'abstract': False,
                'default_related_name': 'filter_set_type_rules',
                'db_table': 'filter_set_type_rule',
            },
        ),
    ]
