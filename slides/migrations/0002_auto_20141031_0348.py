# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='title',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='date',
            field=models.DateField(default=datetime.date(2014, 10, 31)),
            preserve_default=True,
        ),
    ]
