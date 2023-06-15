from django.shortcuts import render
from rest_framework import viewsets
from drivers.models import *
from drivers.serializers import *

# Create your views here.


def render_index(request):
    return render(request, 'drivers/index.html')


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer


class EmployeeFileViewSet(viewsets.ModelViewSet):
    queryset = EmployeeFile.objects.all()
    serializer_class = EmployeeFileModelSerializer


class OwnerEmployeeNotificationViewSet(viewsets.ModelViewSet):
    queryset = OwnerEmployeeNotification.objects.all()
    serializer_class = OwnerEmployeeNotificationModelSerializer


class MedicalTestCenterViewSet(viewsets.ModelViewSet):
    queryset = MedicalTestCenter.objects.all()
    serializer_class = MedicalTestCenterModelSerializer


class DotDrugTestViewSet(viewsets.ModelViewSet):
    queryset = DotDrugTest.objects.all()
    serializer_class = DotDrugTestModelSerializer


class MedicalTestFormsViewSet(viewsets.ModelViewSet):
    queryset = MedicalTestForm.objects.all()
    serializer_class = MedicalTestFormModelSerializer


class MedicalTestFormsViewSet(viewsets.ModelViewSet):
    queryset = MedicalTestForm.objects.all()
    serializer_class = MedicalTestFormModelSerializer
