from django.contrib import admin
# Register your models here.
from testapp.models import Hydjobs
class HydAdmin(admin.ModelAdmin):
    list_display =['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Hydjobs,HydAdmin)

from testapp.models import Bngjobs
class BngAdmin(admin.ModelAdmin):
    list_display =['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Bngjobs,BngAdmin)

from testapp.models import Punejobs
class PuneAdmin(admin.ModelAdmin):
    list_display =['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Punejobs,PuneAdmin)
