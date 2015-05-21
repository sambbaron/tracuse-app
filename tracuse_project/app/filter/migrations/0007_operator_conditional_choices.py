# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0006_element_value_rename_elvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterruleassociation',
            name='conditional',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('and', 'and'), ('or', 'or')]),
        ),
        migrations.AlterField(
            model_name='filterruleassociation',
            name='operator',
            field=models.CharField(max_length=5, choices=[('iexact', 'equals'), ('Text', (('contains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))], default='iexact'),
        ),
        migrations.AlterField(
            model_name='filterruleelement',
            name='conditional',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('and', 'and'), ('or', 'or')]),
        ),
        migrations.AlterField(
            model_name='filterruleelement',
            name='operator',
            field=models.CharField(max_length=5, choices=[('iexact', 'equals'), ('Text', (('contains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))], default='iexact'),
        ),
        migrations.AlterField(
            model_name='filterrulegroup',
            name='conditional',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('and', 'and'), ('or', 'or')]),
        ),
        migrations.AlterField(
            model_name='filterrulegroup',
            name='operator',
            field=models.CharField(max_length=5, choices=[('iexact', 'equals'), ('Text', (('contains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))], default='iexact'),
        ),
        migrations.AlterField(
            model_name='filterruletype',
            name='conditional',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('and', 'and'), ('or', 'or')]),
        ),
        migrations.AlterField(
            model_name='filterruletype',
            name='operator',
            field=models.CharField(max_length=5, choices=[('iexact', 'equals'), ('Text', (('contains', 'contains'), ('istartswith', 'starts with'), ('iendswith', 'ends with'))), ('Number', (('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'))), ('Datetime', (('year', 'year'), ('month', 'month'), ('day', 'day'), ('week_day', 'weekday'), ('hour', 'hour'), ('minute', 'minute')))], default='iexact'),
        ),
    ]
