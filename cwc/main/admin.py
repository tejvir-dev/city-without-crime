from django.contrib import admin
from main.models import *

# Register your models here.

admin.site.register(LoginMaster)
admin.site.register(PoliceStationMaster)
admin.site.register(Emergency)
admin.site.register(Complaint)
admin.site.register(CriminalMaster)