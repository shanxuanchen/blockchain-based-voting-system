# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-17 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.CharField(max_length=120),
        ),
    ]
