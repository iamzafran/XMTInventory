from django.db import models
from Ownership.models import XMTStaff, Customer, CustomerLocation, TenantLocation, Department, Developers

# Create your models here.


class Monitor(models.Model):
    serialNo = models.CharField(max_length=120)
    tagNo = models.CharField(max_length=120)
    age = models.CharField(max_length=3)


class Projector(models.Model):
    projectorModel = models.CharField(max_length=120)
    projectorYear = models.CharField(max_length=5)
    projectorTag = models.CharField(max_length=120)
    projectorSerialNumber = models.CharField(max_length=100, null=True, default=None, blank=True)
    tenantlocation = models.ForeignKey(TenantLocation, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    customerLocation = models.ForeignKey(CustomerLocation, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    startDate = models.DateField(null=True, default=None, blank=True)
    endDate = models.DateField(null=True, default=None, blank=True)


class Computer(models.Model):
    pcModel = models.CharField(max_length=25, null=True, default=None, blank=True)
    pcTagNo = models.CharField(max_length=120)
    pcModelSeries = models.CharField(max_length=25, null=True, default=None, blank=True)
    pcName = models.CharField(max_length=120)  #edit
    serialNo = models.CharField(max_length=120)
    operatingSystem = models.CharField(max_length=120) #edit
    processor = models.CharField(max_length=120)
    systemType = models.CharField(max_length=10)
    ram = models.CharField(max_length=8)  #edit
    hardDrive = models.CharField(max_length=10) #edit
    remarks = models.CharField(max_length=250) #edit
    projector = models.ForeignKey(Projector, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    monitor = models.ForeignKey(Monitor, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    xmtstaff = models.ForeignKey(XMTStaff, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    tenantlocation = models.ForeignKey(TenantLocation, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    customerLocation = models.ForeignKey(CustomerLocation, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    startDate = models.DateField(null=True, default=None, blank=True)
    endDate = models.DateField(null=True, default=None, blank=True)

    def __str__(self):
        return self.pcTagNo


class System(models.Model):
    systemName = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    tenantlocation = models.ManyToManyField(TenantLocation)
    xmtstaff = models.ForeignKey(XMTStaff, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    customerLocation = models.ManyToManyField(CustomerLocation)
    developer = models.ForeignKey(Developers, on_delete=models.SET_NULL, null=True, default=None, blank=True)

    def __str__(self):
        return self.systemName


class Email(models.Model):
    licenses = models.CharField(max_length=120)
    principalName = models.CharField(max_length=120)
    dateCreated = models.CharField(max_length=120)
    xmtstaff = models.ForeignKey(XMTStaff, on_delete=models.SET_NULL,
                                 null=True, default=None, blank=True, related_name="+")

    def __str__(self):
        return self.principalName


class Server(models.Model):
    tagNumber = models.CharField(max_length=255)
    hostname = models.CharField(max_length=120)
    serverModel = models.CharField(max_length=120)
    ipv4 = models.CharField(max_length=15)
    domain = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    operatingSystem = models.CharField(max_length=120)
    serialNumber = models.CharField(max_length=120)
    productKey = models.CharField(max_length=250)
    processor = models.CharField(max_length=120)
    hardDrive = models.CharField(max_length=8)
    application = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    tenantlocation = models.ForeignKey(TenantLocation, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    customerLocation = models.ForeignKey(CustomerLocation, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    startDate = models.DateField(null=True, default=None, blank=True)
    endDate = models.DateField(null=True, default=None, blank=True)

    def __str__(self):
        return self.hostname


class DCAsset(models.Model):
    equipment = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    serialNumber = models.CharField(max_length=120)


class Software(models.Model):
    softwareName = models.CharField(max_length=120)
    developer = models.ForeignKey(Developers, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    tenantlocation = models.ManyToManyField(TenantLocation)
    customerLocation = models.ManyToManyField(CustomerLocation)


class DataCenter(models.Model):
    tenantlocation = models.ForeignKey(TenantLocation, on_delete=models.CASCADE, null=True, default=None, blank=True)
    customerLocation = models.ForeignKey(CustomerLocation, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    dataCenter = models.IntegerField()
    numberOfRacks = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()