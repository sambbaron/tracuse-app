# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filterruleassociation',
            options={'verbose_name': 'Filter Rule - Association'},
        ),
        migrations.AlterModelOptions(
            name='filterruleelement',
            options={'verbose_name': 'Filter Rule - Element'},
        ),
        migrations.AlterModelOptions(
            name='filterrulegroup',
            options={'verbose_name': 'Filter Rule - Group'},
        ),
        migrations.AlterModelOptions(
            name='filterruletype',
            options={'verbose_name': 'Filter Rule - Type'},
        ),
        migrations.AlterModelOptions(
            name='filterset',
            options={'verbose_name': 'Filter Set'},
        ),
        migrations.AlterField(
            model_name='filterruleassociation',
            name='association_direction',
            field=models.ForeignKey(db_column='association_direction_id', to='association.AssociationDirection', related_name='filter_rule_associations'),
        ),
        migrations.AlterField(
            model_name='filterruleassociation',
            name='association_type_id',
            field=models.ForeignKey(db_column='association_type_id', to='association.AssociationType', related_name='filter_rule_associations'),
        ),
        migrations.AlterField(
            model_name='filterruleassociation',
            name='datum_object',
            field=models.ForeignKey(db_column='datum_object_id', to='datum.DatumObject', related_name='filter_rule_associations'),
        ),
        migrations.AlterField(
            model_name='filterruleelement',
            name='element_type',
            field=models.ForeignKey(db_column='element_type_id', to='element_type.ElementType', related_name='filter_rule_elements'),
        ),
        migrations.AlterField(
            model_name='filterrulegroup',
            name='datum_group',
            field=models.ForeignKey(db_column='datum_group_id', to='datum.DatumGroup', related_name='filter_rule_groups'),
        ),
        migrations.AlterField(
            model_name='filterruletype',
            name='datum_type',
            field=models.ForeignKey(db_column='datum_type_id', to='datum.DatumType', related_name='filter_rule_types'),
        ),
        migrations.AlterField(
            model_name='filterset',
            name='user_id',
            field=models.ForeignKey(blank=True, db_column='user_id', null=True, to=settings.AUTH_USER_MODEL, related_name='filter_sets'),
        ),
        migrations.AlterField(
            model_name='filtersetassociationrule',
            name='filter_rule_association_id',
            field=models.ForeignKey(db_column='filter_rule_association_id', to='filter.FilterRuleAssociation'),
        ),
        migrations.AlterField(
            model_name='filtersetelementrule',
            name='filter_rule_element_id',
            field=models.ForeignKey(db_column='filter_rule_element_id', to='filter.FilterRuleElement'),
        ),
        migrations.AlterField(
            model_name='filtersetgrouprule',
            name='filter_rule_group_id',
            field=models.ForeignKey(db_column='filter_rule_group_id', to='filter.FilterRuleGroup'),
        ),
        migrations.AlterField(
            model_name='filtersettyperule',
            name='filter_rule_type_id',
            field=models.ForeignKey(db_column='filter_rule_type_id', to='filter.FilterRuleType'),
        ),
    ]
