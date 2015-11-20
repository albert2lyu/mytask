#! /usr/bin/python
# coding=utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

SearchResult = ( \
		(u'未检索', u'未检索'), 
		(u'X', u'X'), \
		(u'Y', u'Y'), \
		(u'XY', u'XY'), \
		(u'RX', u'RX'), \
		(u'RY', u'RY'), \
		(u'RXY', u'RXY'), \
		(u'A', u'A'), \
		(u'R', u'R') )

class PatentItem(models.Model):
	appNO = models.CharField(u'申请号', max_length = 13, default = u'无')
	appIPC = models.CharField(u'分类号', max_length = 15, default = u'无')
	appTaskRatio = models.FloatField(u'平衡系数', default = 1.0)
	appName = models.CharField(u'发明名称', max_length = 100, default = u'无')
	appApplicant = models.CharField(u'申请人', max_length = 100, default = u'无')
	appNation = models.CharField(u'国别', max_length = 10, default = u'无')
	appDate = models.DateField(u'申请日', default = timezone.now())
	theExaminer = models.ForeignKey(User)
	firstActionSearch = models.CharField(u'一通检索结果', max_length = 4, choices = SearchResult, default = u'无')
	firstActionExaminate = models.TextField(u'一通评述', max_length = 50, default = u'无')
	firstActionForecast = models.TextField(u'一通后预计', max_length = 50, default = u'无')
	firstActionDate = models.DateField(u'一通日期', default = timezone.now())
	firstActionReply = models.TextField(u'一通意见陈述', max_length = 100, default = u'无')
	secondActionSearch = models.CharField(u'二通补充检索', max_length = 4, choices = SearchResult, default = u'无')
	secondActionDate = models.DateField(u'二通日期', default = timezone.now())
	secondActionExaminate = models.TextField(u'二通评述', max_length = 50, default = u'无')
	secondActionReply = models.TextField(u'二通意见陈述', max_length = 100, default = u'无')
	thirdActionSearch = models.CharField(u'三通补充检索', max_length = 4, choices = SearchResult, default = u'无')
	thirdActionExaminate = models.TextField(u'三通评述', max_length = 50, default = u'无')
	thirdActionDate = models.DateField(u'三通日期', default = timezone.now())
	thirdActionReply = models.TextField(u'三通意见陈述', max_length = 100, default = u'无')
	fourthActionSearch = models.CharField(u'四通补充检索', max_length = 4 , choices = SearchResult, default = u'无')
	fourthActionExaminate = models.TextField(u'四通评述', max_length = 50, default = u'无')
	fourthActionDate = models.DateField(u'四通日期', default = timezone.now())
	followAction = models.TextField(u'后续处理', max_length = 100, default = u'无')

	class Meta:
		verbose_name = u'发明信息'
		verbose_name_plural = u'发明信息'
	
