# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0006_remove_commodityinorder_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='share_desc',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='batch',
            name='share_img_url',
            field=models.ImageField(blank=True, upload_to='shareImgUrl'),
        ),
        migrations.AddField(
            model_name='batch',
            name='share_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]