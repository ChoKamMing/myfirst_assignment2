# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-23 22:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kris_app', '0002_dryerasemarker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dryerasemarker',
            old_name='instrtuction',
            new_name='instructor',
        ),
    ]
