# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0010_datumtype_relatedname'),
    ]

    operations = [
        migrations.AddField(
            model_name='datumtype',
            name='icon_class',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
