# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-25 03:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('book', 'user')]),
        ),
    ]
