from django.contrib import admin

from companyapp.models import companydata


class companyadmin(admin.ModelAdmin):
	list_display=['name','mail','phone','time','message']

admin.site.register(companydata,companyadmin)
