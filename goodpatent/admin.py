from django.contrib import admin


from django.contrib import admin

from .models import GoodPatent

class GoodPatentAdmin(admin.ModelAdmin) : 
    list_display = ('theExaminer', 'appNO', 'recReason')
    exclude = []

admin.site.register(GoodPatent, GoodPatentAdmin)
