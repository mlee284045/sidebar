# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0003_auto_20141029_0248'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AddField(
            model_name='resource',
            name='file',
            field=models.FileField(null=True, upload_to=b'media/document', blank=True),
            preserve_default=True,
        ),
    ]
