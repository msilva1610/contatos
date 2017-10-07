# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=254)),
                ('mensagem', models.TextField()),
                ('datapublicacao', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]