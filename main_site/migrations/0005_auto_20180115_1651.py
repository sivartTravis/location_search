# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-15 08:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0004_auto_20171225_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bikelocation',
            name='bikeCity',
        ),
        migrations.RemoveField(
            model_name='bikelocation',
            name='bikeCountry',
        ),
        migrations.RemoveField(
            model_name='bikelocation',
            name='bikeDistrict',
        ),
        migrations.RemoveField(
            model_name='bikelocation',
            name='bikeProvince',
        ),
    ]
