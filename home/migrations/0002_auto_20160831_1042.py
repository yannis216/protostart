# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-31 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='logo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='cooperation_partners',
            field=models.TextField(blank=True),
        ),
    ]
