# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('association', '0001_initial'),
        ('datum', '0003_datum_object_associations'),
        ('element_type', '0004_elementtypedatumobject'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterRuleAssociation',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('operator', models.CharField(default='=', max_length=5)),
                ('conditional', models.CharField(blank=True, null=True, choices=[('AND', 'AND'), ('OR', 'OR')], max_length=3)),
                ('filter_rule_association_id', models.AutoField(serialize=False, primary_key=True)),
                ('depth', models.IntegerField(default=1)),
                ('association_direction', models.ForeignKey(db_column='association_direction_id', to='association.AssociationDirection')),
                ('association_type_id', models.ForeignKey(db_column='association_type_id', to='association.AssociationType')),
                ('datum_object', models.ForeignKey(db_column='datum_object_id', to='datum.DatumObject')),
            ],
            options={
                'abstract': False,
                'db_table': 'filter_rule_association',
            },
        ),
        migrations.CreateModel(
            name='FilterRuleElement',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('operator', models.CharField(default='=', max_length=5)),
                ('conditional', models.CharField(blank=True, null=True, choices=[('AND', 'AND'), ('OR', 'OR')], max_length=3)),
                ('filter_rule_element_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_value', models.CharField(max_length=255)),
                ('element_type', models.ForeignKey(db_column='element_type_id', to='element_type.ElementType')),
            ],
            options={
                'abstract': False,
                'db_table': 'filter_rule_element',
            },
        ),
        migrations.CreateModel(
            name='FilterRuleGroup',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('operator', models.CharField(default='=', max_length=5)),
                ('conditional', models.CharField(blank=True, null=True, choices=[('AND', 'AND'), ('OR', 'OR')], max_length=3)),
                ('filter_rule_group_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_group', models.ForeignKey(db_column='datum_group_id', to='datum.DatumGroup')),
            ],
            options={
                'abstract': False,
                'db_table': 'filter_rule_group',
            },
        ),
        migrations.CreateModel(
            name='FilterRuleType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('operator', models.CharField(default='=', max_length=5)),
                ('conditional', models.CharField(blank=True, null=True, choices=[('AND', 'AND'), ('OR', 'OR')], max_length=3)),
                ('filter_rule_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_type', models.ForeignKey(db_column='datum_type_id', to='datum.DatumType')),
            ],
            options={
                'abstract': False,
                'db_table': 'filter_rule_type',
            },
        ),
        migrations.CreateModel(
            name='FilterSet',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', db_index=True, max_length=25)),
                ('short_definition', models.CharField(blank=True, null=True, max_length=25)),
                ('long_definition', models.CharField(blank=True, null=True, max_length=100)),
                ('filter_set_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, db_column='user_id')),
            ],
            options={
                'abstract': False,
                'db_table': 'filter_set',
            },
        ),
        migrations.CreateModel(
            name='FilterSetAssociationRule',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('filter_set_association_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_association_id', models.ForeignKey(to='filter.FilterRuleAssociation')),
                ('filter_set_id', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'abstract': False,
                'db_table': 'filter_set_association_rule',
            },
        ),
        migrations.CreateModel(
            name='FilterSetElementRule',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('filter_set_element_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_element_id', models.ForeignKey(to='filter.FilterRuleElement')),
                ('filter_set_id', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'abstract': False,
                'db_table': 'filter_set_element_rule',
            },
        ),
        migrations.CreateModel(
            name='FilterSetGroupRule',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('filter_set_group_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_group_id', models.ForeignKey(to='filter.FilterRuleGroup')),
                ('filter_set_id', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'abstract': False,
                'db_table': 'filter_set_group_rule',
            },
        ),
        migrations.CreateModel(
            name='FilterSetTypeRule',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('filter_set_type_rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('filter_rule_type_id', models.ForeignKey(to='filter.FilterRuleType')),
                ('filter_set_id', models.ForeignKey(db_column='filter_set_id', to='filter.FilterSet')),
            ],
            options={
                'abstract': False,
                'db_table': 'filter_set_type_rule',
            },
        ),
    ]
