from django.contrib import admin
from apps.RRHH.models import *
# Register your models here.

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Attendance)
admin.site.register(Employee)
admin.site.register(ContractorEmployee)