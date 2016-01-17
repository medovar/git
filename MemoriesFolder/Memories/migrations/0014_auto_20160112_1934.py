# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Memories', '0013_auto_20160112_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_st', models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameField(
            model_name='mem',
            old_name='like',
            new_name='like_count',
        ),
        migrations.AddField(
            model_name='like',
            name='mem',
            field=models.ForeignKey(to='Memories.Mem'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
