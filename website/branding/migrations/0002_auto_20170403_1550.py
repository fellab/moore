# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 13:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branding', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logo',
            options={'verbose_name': 'logo', 'verbose_name_plural': 'logos'},
        ),
        migrations.AlterModelOptions(
            name='socialmediasettings',
            options={'verbose_name': 'social media accounts'},
        ),
    ]