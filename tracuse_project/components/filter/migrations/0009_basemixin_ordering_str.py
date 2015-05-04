# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0008_basemixin_ordering_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filterruleassociation',
            options={'ordering': ['sort', '__str__'], 'verbose_name': 'Filter Rule - Association'},
        ),
        migrations.AlterModelOptions(
            name='filterruleelement',
            options={'ordering': ['sort', '__str__'], 'verbose_name': 'Filter Rule - Element'},
        ),
        migrations.AlterModelOptions(
            name='filterrulegroup',
            options={'ordering': ['sort', '__str__'], 'verbose_name': 'Filter Rule - Group'},
        ),
        migrations.AlterModelOptions(
            name='filterruletype',
            options={'ordering': ['sort', '__str__'], 'verbose_name': 'Filter Rule - Type'},
        ),
        migrations.AlterModelOptions(
            name='filtersetassociationrule',
            options={'ordering': ['sort', '__str__']},
        ),
        migrations.AlterModelOptions(
            name='filtersetelementrule',
            options={'ordering': ['sort', '__str__']},
        ),
        migrations.AlterModelOptions(
            name='filtersetgrouprule',
            options={'ordering': ['sort', '__str__']},
        ),
        migrations.AlterModelOptions(
            name='filtersettyperule',
            options={'ordering': ['sort', '__str__']},
        ),
    ]
