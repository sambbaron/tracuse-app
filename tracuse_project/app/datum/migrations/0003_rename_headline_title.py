# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0002_auto_20150707_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datumtype',
            old_name='title_expression',
            new_name='title_expression',
        ),
    ]
