from rest_framework import serializers
from Inventory.models import *
from Ownership.models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        field = ('id', 'departmentName')


class StaffSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Staff
        field = ('id', 'staffID' 'staffName', 'position', 'location')


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        field = ('id', 'tenantName')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        field = ('id', 'projectName')


class ProjectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projector
        fields = '__all__'


class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'


class ComputerSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    department = DepartmentSerializer()
    tenant = TenantSerializer()
    project = ProjectSerializer()
    projector = ProjectorSerializer()
    monitor = MonitorSerializer()

    class Meta:
        model = Computer
        fields = '__all__'


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        field = ('id', 'systemName', 'location')


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        field = ('id', 'licenses', 'principalName', 'dateCreated')


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        field = ('id', 'hostname', 'serverModel', 'ipv4', 'domain', 'username', 'password', 'operatingSystem',
                 'serialNumber', 'productKey', 'processor', 'hardDrive', 'application', 'location')


class DCAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DCAsset
        field = ('id', 'equipment', 'description', 'serialNumber')


class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        field = ('id', 'softwareName')


class SoftwareOwnershipSerializer(serializers.ModelSerializer):
    software = SoftwareSerializer()
    staff = StaffSerializer()





