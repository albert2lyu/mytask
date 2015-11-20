# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExaminateTip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipContent', models.TextField(default='\u65e0', max_length=500, verbose_name='\u5185\u5bb9')),
                ('submitTime', models.DateTimeField(default=datetime.datetime(2015, 11, 8, 7, 38, 54, 624000, tzinfo=utc), verbose_name='\u63d0\u4ea4\u65f6\u95f4')),
                ('theExaminer', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u5ba1\u67e5\u539f\u5219\u53ca\u6280\u5de7',
                'verbose_name_plural': '\u5ba1\u67e5\u539f\u5219\u53ca\u6280\u5de7',
            },
        ),
        migrations.CreateModel(
            name='TipCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoryName', models.CharField(default='\u65e0', max_length=20, verbose_name='\u5ba1\u67e5\u65b9\u9762')),
            ],
            options={
                'verbose_name': '\u6cd5\u6761\u54ea\u65b9\u9762',
                'verbose_name_plural': '\u6cd5\u6761\u54ea\u65b9\u9762',
            },
        ),
        migrations.AddField(
            model_name='examinatetip',
            name='tipCategory',
            field=models.ForeignKey(to='examinatetips.TipCategory'),
        ),
    ]
