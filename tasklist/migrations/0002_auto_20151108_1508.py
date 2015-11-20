# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patentitem',
            name='appDate',
            field=models.DateField(default=datetime.datetime(2015, 11, 8, 7, 8, 3, 741000, tzinfo=utc), verbose_name='\u7533\u8bf7\u65e5'),
        ),
        migrations.AlterField(
            model_name='patentitem',
            name='firstActionDate',
            field=models.DateField(default=datetime.datetime(2015, 11, 8, 7, 8, 3, 741000, tzinfo=utc), verbose_name='\u4e00\u901a\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='patentitem',
            name='fourthActionDate',
            field=models.DateField(default=datetime.datetime(2015, 11, 8, 7, 8, 3, 741000, tzinfo=utc), verbose_name='\u56db\u901a\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='patentitem',
            name='secondActionDate',
            field=models.DateField(default=datetime.datetime(2015, 11, 8, 7, 8, 3, 741000, tzinfo=utc), verbose_name='\u4e8c\u901a\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='patentitem',
            name='thirdActionDate',
            field=models.DateField(default=datetime.datetime(2015, 11, 8, 7, 8, 3, 741000, tzinfo=utc), verbose_name='\u4e09\u901a\u65e5\u671f'),
        ),
    ]
