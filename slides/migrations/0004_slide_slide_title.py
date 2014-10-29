# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0003_auto_20141028_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='slide_title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
