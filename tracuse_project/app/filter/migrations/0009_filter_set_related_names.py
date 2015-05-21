# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0008_filterset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filtersetassociationrule',
            name='filter_rule_association_id',
        ),
        migrations.RemoveField(
            model_name='filtersetassociationrule',
            name='filter_set_id',
        ),
        migrations.RemoveField(
            model_name='filtersetelementrule',
            name='filter_rule_element_id',
        ),
        migrations.RemoveField(
            model_name='filtersetelementrule',
            name='filter_set_id',
        ),
        migrations.RemoveField(
            model_name='filtersetgrouprule',
            name='filter_rule_group_id',
        ),
        migrations.RemoveField(
            model_name='filtersetgrouprule',
            name='filter_set_id',
        ),
        migrations.RemoveField(
            model_name='filtersettyperule',
            name='filter_rule_type_id',
        ),
        migrations.RemoveField(
            model_name='filtersettyperule',
            name='filter_set_id',
        ),
        migrations.AddField(
            model_name='filtersetassociationrule',
            name='filter_rule_association',
            field=models.ForeignKey(default=0, to='filter.FilterRuleAssociation', db_column='filter_rule_association_id', related_name='filter_set_association_rules'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtersetassociationrule',
            name='filter_set',
            field=models.ForeignKey(default='', to='filter.FilterSet', db_column='filter_set_id', related_name='filter_set_association_rules'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtersetelementrule',
            name='filter_rule_element',
            field=models.ForeignKey(default='', to='filter.FilterRuleElement', db_column='filter_rule_element_id', related_name='filter_set_element_rules'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtersetelementrule',
            name='filter_set',
            field=models.ForeignKey(default='', to='filter.FilterSet', db_column='filter_set_id', related_name='filter_set_element_rules'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtersetgrouprule',
            name='filter_rule_group',
            field=models.ForeignKey(default='', to='filter.FilterRuleGroup', db_column='filter_rule_group_id', related_name='filter_set_group_rules'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtersetgrouprule',
            name='filter_set',
            field=models.ForeignKey(default='', to='filter.FilterSet', db_column='filter_set_id', related_name='filter_set_group_rules'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtersettyperule',
            name='filter_rule_type',
            field=models.ForeignKey(default='', to='filter.FilterRuleType', db_column='filter_rule_type_id', related_name='filter_set_type_rules'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtersettyperule',
            name='filter_set',
            field=models.ForeignKey(default='', to='filter.FilterSet', db_column='filter_set_id', related_name='filter_set_type_rules'),
            preserve_default=False,
        ),
    ]
