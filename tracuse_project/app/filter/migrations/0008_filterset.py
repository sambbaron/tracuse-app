from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0007_operator_conditional_choices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filterset',
            old_name='user_id',
            new_name='user',
        ),
    ]
