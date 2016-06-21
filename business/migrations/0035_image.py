# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0034_remove_recipe_dish_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('md5', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/upload/%Y/%m/%d')),
            ],
        ),
    ]
