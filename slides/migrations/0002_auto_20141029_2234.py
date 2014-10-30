# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=b'profile/pictures', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='file',
            field=models.FileField(null=True, upload_to=b'document', blank=True),
            preserve_default=True,
        ),
    ]
