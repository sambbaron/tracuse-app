# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0011_filterrule_operator_icontains'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterruleassociation',
            name='operator',
            field=models.CharField(default='exact', choices=[('exact', 'equals'), ('Text', (('iexact', 'text equals'), ('icontains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))], max_length=5),
        ),
        migrations.AlterField(
            model_name='filterruleelement',
            name='operator',
            field=models.CharField(default='exact', choices=[('exact', 'equals'), ('Text', (('iexact', 'text equals'), ('icontains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))], max_length=5),
        ),
        migrations.AlterField(
            model_name='filterrulegroup',
            name='operator',
            field=models.CharField(default='exact', choices=[('exact', 'equals'), ('Text', (('iexact', 'text equals'), ('icontains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))], max_length=5),
        ),
        migrations.AlterField(
            model_name='filterruletype',
            name='operator',
            field=models.CharField(default='exact', choices=[('exact', 'equals'), ('Text', (('iexact', 'text equals'), ('icontains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))], max_length=5),
        ),
    ]
