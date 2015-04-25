# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0004_datumtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datumgroup',
            name='datum_group_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
