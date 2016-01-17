# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Memories', '0011_auto_20160112_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
