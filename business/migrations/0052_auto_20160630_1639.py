# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 08:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0051_bulk_receive_mode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exhibitedproduct',
            old_name='cover',
            new_name='cover_2x',
        ),
    ]
