# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 22:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Contato',
        ),
    ]
