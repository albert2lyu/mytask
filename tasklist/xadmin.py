#from django.contrib import admin

from .models import PatentItem
from .xadmin import xadmin

class PatentItemAdmin(object):
	fields = ['appNO', 'appIPC', 'appName', \
		'appApplicant', 'appDate', 'appNation', \
		'firstActionSearch', 'firstActionExaminate', \
		'firstActionForecast', 'firstActionDate', 'firstActionReply', \
		'secondActionSearch', 'secondActionExaminate', \
		'secondActionDate', \
		'secondActionReply', \
		'thirdActionSearch', 'thirdActionExaminate', 'thirdActionDate', \
		'thirdActionReply', 'fourthActionSearch', \
		'fourthActionExaminate', 'fourthActionDate', 'followAction']
	list_display = ('appNO', 'appName', 'appDate', \
		'appApplicant', 'firstActionSearch', \
		'firstActionExaminate', 'secondActionExaminate', \
		'thirdActionExaminate', 'fourthActionExaminate')
xadmin.site.register(PatentItem, PatentItemAdmin)
