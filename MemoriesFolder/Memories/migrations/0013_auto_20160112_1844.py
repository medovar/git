# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Memories', '0012_comments_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='like',
        ),
        migrations.AddField(
            model_name='mem',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
