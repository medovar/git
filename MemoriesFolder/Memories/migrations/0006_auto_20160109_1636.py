# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Memories', '0005_mem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mem',
            name='person',
        ),
        migrations.DeleteModel(
            name='Mem',
        ),
    ]