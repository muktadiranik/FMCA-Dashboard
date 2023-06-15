from django.contrib import admin
from drivers.models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(EmployeeFile)
admin.site.register(OwnerEmployeeNotification)
admin.site.register(MedicalTestCenter)
admin.site.register(DotDrugTest)
admin.site.register(MedicalTestForm)
