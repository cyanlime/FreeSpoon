# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0049_auto_20160624_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='recent_dispatcher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Dispatcher'),
        ),
    ]