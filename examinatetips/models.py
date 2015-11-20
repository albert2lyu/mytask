#! /usr/bin/python
# coding=utf-8

from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

class TipCategory(models.Model):
	categoryName = models.CharField(u'审查方面', max_length = 20, default = u'无')
	
	class Meta:
		verbose_name = u'审查涉及法条及问题的类型'
		verbose_name_plural = u'审查涉及法条及问题的类型'
		
	def __str__(self):
		return self.categoryName.encode('utf-8')
	
	
		

class ExaminateTip(models.Model):
	tipCategory = models.ForeignKey(TipCategory)
	tipContent = models.TextField(u'内容', max_length = 500, default = u'无')
	theExaminer = models.ForeignKey(User, null = True)
	submitTime = models.DateTimeField(u'提交时间', default = timezone.now())
	
	class Meta:
		verbose_name = u'审查原则及技巧'
		verbose_name_plural = u'审查原则及技巧'
		
	def __str__(self):
		return 'examinate tip'
