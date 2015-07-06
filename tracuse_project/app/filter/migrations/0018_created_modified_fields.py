# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0017_filterset_rules_m2m'),
    ]

    operations = [
        migrations.AddField(
            model_name='filterruleassociation',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filterruleassociation',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 42, 679377, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filterruledatatype',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filterruledatatype',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 45, 250524, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filterruleelement',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filterruleelement',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 46, 953621, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filterrulegroup',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filterrulegroup',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 48, 673720, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filterruletype',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filterruletype',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 50, 327814, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filterruleuser',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filterruleuser',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 51, 953907, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filterset',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filterset',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 53, 619003, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtersetassociationrule',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filtersetassociationrule',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 55, 725123, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtersetdatatyperule',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filtersetdatatyperule',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 57, 388218, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtersetelementrule',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filtersetelementrule',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 8, 58, 956308, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtersetgrouprule',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filtersetgrouprule',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 9, 0, 506397, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtersettyperule',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filtersettyperule',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 9, 1, 960480, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtersetuserrule',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filtersetuserrule',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 6, 23, 9, 3, 366560, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
