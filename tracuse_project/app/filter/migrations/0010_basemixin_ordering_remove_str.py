# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0009_basemixin_ordering_str'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filterruleassociation',
            options={'ordering': ['sort'], 'verbose_name': 'Filter Rule - Association'},
        ),
        migrations.AlterModelOptions(
            name='filterruleelement',
            options={'ordering': ['sort'], 'verbose_name': 'Filter Rule - Element'},
        ),
        migrations.AlterModelOptions(
            name='filterrulegroup',
            options={'ordering': ['sort'], 'verbose_name': 'Filter Rule - Group'},
        ),
        migrations.AlterModelOptions(
            name='filterruletype',
            options={'ordering': ['sort'], 'verbose_name': 'Filter Rule - Type'},
        ),
        migrations.AlterModelOptions(
            name='filtersetassociationrule',
            options={'ordering': ['sort']},
        ),
        migrations.AlterModelOptions(
            name='filtersetelementrule',
            options={'ordering': ['sort']},
        ),
        migrations.AlterModelOptions(
            name='filtersetgrouprule',
            options={'ordering': ['sort']},
        ),
        migrations.AlterModelOptions(
            name='filtersettyperule',
            options={'ordering': ['sort']},
        ),
    ]
