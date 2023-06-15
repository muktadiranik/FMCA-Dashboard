from rest_framework import serializers
from drivers.models import *


class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeFileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeFile
        fields = '__all__'


class OwnerEmployeeNotificationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerEmployeeNotification
        fields = '__all__'


class MedicalTestCenterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTestCenter
        fields = '__all__'


class DotDrugTestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DotDrugTest
        fields = '__all__'


class MedicalTestFormModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTestForm
        fields = '__all__'
