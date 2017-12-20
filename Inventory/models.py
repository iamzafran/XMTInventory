from django.db import models

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


class Computer(models.Model):
    pcTagNo = models.CharField(max_length=120)
    pcName = models.CharField(max_length=120)
    serialNo = models.CharField(max_length=120)
    operatingSystem = models.CharField(max_length=120)
    processor = models.CharField(max_length=120)
    systemType = models.CharField(max_length=10)
    ram = models.CharField(max_length=8)
    hardDrive = models.CharField(max_length=10)
    remarks = models.CharField(max_length=250)
    projector = models.ForeignKey(Projector, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    monitor = models.ForeignKey(Monitor, on_delete=models.SET_NULL, null=True, default=None, blank=True)


class System(models.Model):
    systemName = models.CharField(max_length=120)
    location = models.CharField(max_length=120)


class Email(models.Model):
    licenses = models.CharField(max_length=120)
    principalName = models.CharField(max_length=120)
    dateCreated = models.CharField(max_length=120)


class Server(models.Model):
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


class DCAsset(models.Model):
    equipment = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    serialNumber = models.CharField(max_length=120)


class Software(models.Model):
    softwareName = models.CharField(max_length=120)


