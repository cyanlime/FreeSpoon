# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0004_auto_20160323_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='avatar',
            field=models.CharField(default='about:blank', max_length=200),
            preserve_default=False,
        ),
    ]