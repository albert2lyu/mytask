#! /usr/bin/python
# coding=utf-8

from django.contrib import admin

# to use django-import-export
from import_export import resources
from import_export.admin import ImportExportModelAdmin


from .models import PatentItem
#from .xadmin import xadmin

# to use django-import-export
class PatentItemResource(resources.ModelResource) : 
	class Meta : 
		model = PatentItem
class PatentItemAdmin(ImportExportModelAdmin):
    	fieldsets = [
		(u'申请信息', {'fields' : ('appNO', 'appIPC', 'appName', \
		'appApplicant', 'appDate', 'appNation', 'appTaskRatio')}), \
		(None, {'fields' : ['theExaminer']}), \
		(u'一通', {'fields' : ('firstActionSearch', 'firstActionExaminate', \
		'firstActionForecast', 'firstActionDate', 'firstActionReply')}), \
		(u'二通', {'fields' : ('secondActionSearch', 'secondActionExaminate', \
		'secondActionDate', \
		'secondActionReply')}), \
		(u'三通', {'fields' : ('thirdActionSearch', 'thirdActionExaminate', 'thirdActionDate', \
		'thirdActionReply')}), \
		(u'四通', {'fields' : ('fourthActionSearch', \
		'fourthActionExaminate', 'fourthActionDate', 'followAction')}), \
	]
	
	list_display = ('appNO', 'appName', 'appDate', 'appTaskRatio', \
		'appApplicant', \
		#'theExaminer', \
		'firstActionSearch', \
		'firstActionExaminate', 'secondActionExaminate', \
		'thirdActionExaminate', 'fourthActionExaminate')
	list_filter = ['theExaminer', 'appDate']
	search_fields = ['appName']
	save_on_top = True

	resource_class = PatentItemResource
	
	
admin.site.register(PatentItem, PatentItemAdmin)
