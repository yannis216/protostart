# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20160831_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventbrite_link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
