# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 13:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Memories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mem',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
