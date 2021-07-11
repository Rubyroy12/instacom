# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-11 07:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0003_auto_20210711_1036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='Comments',
            new_name='commentor',
        ),
        migrations.AddField(
            model_name='comments',
            name='comments',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
