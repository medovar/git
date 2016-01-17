# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Memories', '0009_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('user_st', models.BooleanField(default=True)),
                ('like', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='mem',
            name='like',
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
