# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-17 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_id', models.CharField(max_length=100)),
                ('validity_period', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PollBlockchain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiverId', models.CharField(max_length=120)),
                ('timeStampVote', models.DateTimeField()),
                ('prevHash', models.CharField(max_length=64)),
                ('blockHash', models.CharField(max_length=64)),
                ('nonce', models.IntegerField()),
            ],
        ),
    ]
