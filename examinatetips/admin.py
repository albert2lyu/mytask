#! /usr/bin/python
# coding=utf-8

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import TipCategory, ExaminateTip

# class TipCategoryAdmin(admin.ModelAdmin):
# 	fields = ['categoryName']
# 	list_display = ['categoryName']
	

class ExaminateTipAdmin(admin.ModelAdmin):
	fields = ['tipCategory', 'tipContent', \
			'theExaminer']
	list_display = ('tipCategory', 'tipContent', 'theExaminer')
	
admin.site.register(ExaminateTip, ExaminateTipAdmin)

class TipCategoryResource(resources.ModelResource) : 
	class Meta : 
		model = TipCategory

class ExaminateTipResource(resources.ModelResource) : 
	class Meta : 
		mode = ExaminateTip

class TipCategoryAdmin(ImportExportModelAdmin) : 
	resource_class = TipCategoryResource
	
admin.site.register(TipCategory, TipCategoryAdmin)
