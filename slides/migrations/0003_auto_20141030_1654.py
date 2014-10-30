# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_auto_20141029_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=b'profile', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='date',
            field=models.DateField(default=datetime.date(2014, 10, 30)),
            preserve_default=True,
        ),
    ]
