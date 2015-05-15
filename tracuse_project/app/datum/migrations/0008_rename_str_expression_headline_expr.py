# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0007_entitymixin_increase_name_len'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datumtype',
            old_name='str_expression',
            new_name='headline_expr',
        ),
    ]
