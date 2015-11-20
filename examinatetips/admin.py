#! /usr/bin/python
# coding=utf-8

from django.contrib import admin

from .models import TipCategory, ExaminateTip

class TipCategoryAdmin(admin.ModelAdmin):
	fields = ['categoryName']
	list_display = ['categoryName']
	
admin.site.register(TipCategory, TipCategoryAdmin)

class ExaminateTipAdmin(admin.ModelAdmin):
	fields = ['tipCategory', 'tipContent', \
			'theExaminer', 'submitTime']
	list_display = ('tipCategory', 'tipContent', 'theExaminer')
	
admin.site.register(ExaminateTip, ExaminateTipAdmin)	
