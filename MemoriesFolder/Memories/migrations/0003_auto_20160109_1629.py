# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Memories', '0002_auto_20160109_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mem',
            name='pud_date',
        ),
        migrations.AddField(
            model_name='mem',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
    ]