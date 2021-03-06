# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 07:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Globe_Mobile_Admin', '0007_auto_20160524_1340'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SMS_Message',
            new_name='Messages',
        ),
        migrations.AlterField(
            model_name='session',
            name='Session_expiry',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 23, 7, 13, 41, 423022, tzinfo=utc), verbose_name='Session expiry'),
        ),
        migrations.AlterField(
            model_name='verification',
            name='last_mod',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 7, 13, 41, 423022, tzinfo=utc), verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='verification',
            name='valid',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 7, 23, 41, 423022, tzinfo=utc), verbose_name='Valid until'),
        ),
    ]
