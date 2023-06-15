from rest_framework import routers
from drivers.views import *

app_name = 'drivers'

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'employeefile', EmployeeFileViewSet)
router.register(r'owneremployeenotification', OwnerEmployeeNotificationViewSet)
router.register(r'medicaltestcenter', MedicalTestCenterViewSet)
router.register(r'dotdrugtest', DotDrugTestViewSet)
router.register(r'medicaltestform', MedicalTestFormsViewSet)


urlpatterns = router.urls
