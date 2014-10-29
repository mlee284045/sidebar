# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_auto_20141028_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(null=True, upload_to=b'media/document', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='staticpage',
            old_name='content',
            new_name='text',
        ),
        migrations.AddField(
            model_name='resource',
            name='title',
            field=models.TextField(default=123, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='date',
            field=models.DateField(default=datetime.date(2014, 10, 29)),
            preserve_default=True,
        ),
    ]
