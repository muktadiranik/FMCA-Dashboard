from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from drivers.models import *
from drivers.serializers import *

# Create your views here.


def render_index(request):
    return render(request, 'drivers/index.html')


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer


class AllEmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['first_name', 'last_name', 'company__name']


class ActiveEmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(is_active=True)
    serializer_class = EmployeeModelSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['first_name', 'last_name', 'company__name']


class InactiveEmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(is_active=False)
    serializer_class = EmployeeModelSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['first_name', 'last_name', 'company__name']


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
