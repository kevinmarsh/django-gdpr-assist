# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-07-17 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("missing_anonymised_migration", "0001_initial")]

    operations = [
        migrations.RemoveField(model_name="modelwithprivacymeta", name="anonymised")
    ]