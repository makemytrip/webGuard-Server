# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_zapinstance_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapinstance',
            name='session',
            field=models.CharField(default='2cc4d04a-e148-4eee-b41b-1ed589f081b0', max_length=255, verbose_name='Session'),
            preserve_default=False,
        ),
    ]
