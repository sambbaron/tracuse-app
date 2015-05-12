# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0005_basemixin_ordering_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filterruleassociation',
            options={'verbose_name': 'Filter Rule - Association', 'ordering': ('-sort',)},
        ),
        migrations.AlterModelOptions(
            name='filterruleelement',
            options={'verbose_name': 'Filter Rule - Element', 'ordering': ('-sort',)},
        ),
        migrations.AlterModelOptions(
            name='filterrulegroup',
            options={'verbose_name': 'Filter Rule - Group', 'ordering': ('-sort',)},
        ),
        migrations.AlterModelOptions(
            name='filterruletype',
            options={'verbose_name': 'Filter Rule - Type', 'ordering': ('-sort',)},
        ),
        migrations.AlterModelOptions(
            name='filtersetassociationrule',
            options={'ordering': ('-sort',)},
        ),
        migrations.AlterModelOptions(
            name='filtersetelementrule',
            options={'ordering': ('-sort',)},
        ),
        migrations.AlterModelOptions(
            name='filtersetgrouprule',
            options={'ordering': ('-sort',)},
        ),
        migrations.AlterModelOptions(
            name='filtersettyperule',
            options={'ordering': ('-sort',)},
        ),
    ]
