# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_units_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='units',
            name='keywords',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
