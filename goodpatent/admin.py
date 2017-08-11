from django.contrib import admin


from django.contrib import admin

from .models import GoodPatent

class GoodPatentAdmin(admin.ModelAdmin) : 
    exclude = []

admin.site.register(GoodPatent, GoodPatentAdmin)
