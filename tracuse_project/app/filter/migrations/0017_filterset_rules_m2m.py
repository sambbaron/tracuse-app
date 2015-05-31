# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0016_entitymodel_names_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='filterset',
            name='filter_rules_association',
            field=models.ManyToManyField(through='filter.FilterSetAssociationRule', related_name='+', to='filter.FilterRuleAssociation'),
        ),
        migrations.AddField(
            model_name='filterset',
            name='filter_rules_data_type',
            field=models.ManyToManyField(through='filter.FilterSetDataTypeRule', related_name='+', to='filter.FilterRuleDataType'),
        ),
        migrations.AddField(
            model_name='filterset',
            name='filter_rules_element',
            field=models.ManyToManyField(through='filter.FilterSetElementRule', related_name='+', to='filter.FilterRuleElement'),
        ),
        migrations.AddField(
            model_name='filterset',
            name='filter_rules_group',
            field=models.ManyToManyField(through='filter.FilterSetGroupRule', related_name='+', to='filter.FilterRuleGroup'),
        ),
        migrations.AddField(
            model_name='filterset',
            name='filter_rules_type',
            field=models.ManyToManyField(through='filter.FilterSetTypeRule', related_name='+', to='filter.FilterRuleType'),
        ),
        migrations.AddField(
            model_name='filterset',
            name='filter_rules_user',
            field=models.ManyToManyField(through='filter.FilterSetUserRule', related_name='+', to='filter.FilterRuleUser'),
        ),
    ]
