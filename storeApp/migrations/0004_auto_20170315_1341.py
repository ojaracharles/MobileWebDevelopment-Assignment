# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0003_auto_20170315_1333'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
    ]
