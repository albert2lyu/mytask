# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatentItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appNO', models.CharField(default='\u65e0', max_length=13, verbose_name='\u7533\u8bf7\u53f7')),
                ('appIPC', models.CharField(default='\u65e0', max_length=15, verbose_name='\u5206\u7c7b\u53f7')),
                ('appTaskRatio', models.FloatField(default=1.0, verbose_name='\u5e73\u8861\u7cfb\u6570')),
                ('appName', models.CharField(default='\u65e0', max_length=100, verbose_name='\u53d1\u660e\u540d\u79f0')),
                ('appApplicant', models.CharField(default='\u65e0', max_length=100, verbose_name='\u7533\u8bf7\u4eba')),
                ('appNation', models.CharField(default='\u65e0', max_length=10, verbose_name='\u56fd\u522b')),
                ('appDate', models.DateField(default=datetime.datetime(2015, 11, 8, 7, 7, 23, 684000, tzinfo=utc), verbose_name='\u7533\u8bf7\u65e5')),
                ('firstActionSearch', models.CharField(default='\u65e0', max_length=4, verbose_name='\u4e00\u901a\u68c0\u7d22\u7ed3\u679c', choices=[('\u672a\u68c0\u7d22', '\u672a\u68c0\u7d22'), ('X', 'X'), ('Y', 'Y'), ('XY', 'XY'), ('RX', 'RX'), ('RY', 'RY'), ('RXY', 'RXY'), ('A', 'A'), ('R', 'R')])),
                ('firstActionExaminate', models.TextField(default='\u65e0', max_length=50, verbose_name='\u4e00\u901a\u8bc4\u8ff0')),
                ('firstActionForecast', models.TextField(default='\u65e0', max_length=50, verbose_name='\u4e00\u901a\u540e\u9884\u8ba1')),
                ('firstActionDate', models.DateField(default=datetime.datetime(2015, 11, 8, 7, 7, 23, 684000, tzinfo=utc), verbose_name='\u4e00\u901a\u65e5\u671f')),
                ('firstActionReply', models.TextField(default='\u65e0', max_length=100, verbose_name='\u4e00\u901a\u610f\u89c1\u9648\u8ff0')),
                ('secondActionSearch', models.CharField(default='\u65e0', max_length=4, verbose_name='\u4e8c\u901a\u8865\u5145\u68c0\u7d22', choices=[('\u672a\u68c0\u7d22', '\u672a\u68c0\u7d22'), ('X', 'X'), ('Y', 'Y'), ('XY', 'XY'), ('RX', 'RX'), ('RY', 'RY'), ('RXY', 'RXY'), ('A', 'A'), ('R', 'R')])),
                ('secondActionDate', models.DateField(default=datetime.datetime(2015, 11, 8, 7, 7, 23, 684000, tzinfo=utc), verbose_name='\u4e8c\u901a\u65e5\u671f')),
                ('secondActionExaminate', models.TextField(default='\u65e0', max_length=50, verbose_name='\u4e8c\u901a\u8bc4\u8ff0')),
                ('secondActionReply', models.TextField(default='\u65e0', max_length=100, verbose_name='\u4e8c\u901a\u610f\u89c1\u9648\u8ff0')),
                ('thirdActionSearch', models.CharField(default='\u65e0', max_length=4, verbose_name='\u4e09\u901a\u8865\u5145\u68c0\u7d22', choices=[('\u672a\u68c0\u7d22', '\u672a\u68c0\u7d22'), ('X', 'X'), ('Y', 'Y'), ('XY', 'XY'), ('RX', 'RX'), ('RY', 'RY'), ('RXY', 'RXY'), ('A', 'A'), ('R', 'R')])),
                ('thirdActionExaminate', models.TextField(default='\u65e0', max_length=50, verbose_name='\u4e09\u901a\u8bc4\u8ff0')),
                ('thirdActionDate', models.DateField(default=datetime.datetime(2015, 11, 8, 7, 7, 23, 684000, tzinfo=utc), verbose_name='\u4e09\u901a\u65e5\u671f')),
                ('thirdActionReply', models.TextField(default='\u65e0', max_length=100, verbose_name='\u4e09\u901a\u610f\u89c1\u9648\u8ff0')),
                ('fourthActionSearch', models.CharField(default='\u65e0', max_length=4, verbose_name='\u56db\u901a\u8865\u5145\u68c0\u7d22', choices=[('\u672a\u68c0\u7d22', '\u672a\u68c0\u7d22'), ('X', 'X'), ('Y', 'Y'), ('XY', 'XY'), ('RX', 'RX'), ('RY', 'RY'), ('RXY', 'RXY'), ('A', 'A'), ('R', 'R')])),
                ('fourthActionExaminate', models.TextField(default='\u65e0', max_length=50, verbose_name='\u56db\u901a\u8bc4\u8ff0')),
                ('fourthActionDate', models.DateField(default=datetime.datetime(2015, 11, 8, 7, 7, 23, 684000, tzinfo=utc), verbose_name='\u56db\u901a\u65e5\u671f')),
                ('followAction', models.TextField(default='\u65e0', max_length=100, verbose_name='\u540e\u7eed\u5904\u7406')),
                ('theExaminer', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u53d1\u660e\u4fe1\u606f',
                'verbose_name_plural': '\u53d1\u660e\u4fe1\u606f',
            },
        ),
    ]
