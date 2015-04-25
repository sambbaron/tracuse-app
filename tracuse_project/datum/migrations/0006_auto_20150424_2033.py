# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0005_auto_20150424_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datumtype',
            name='datum_type_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
