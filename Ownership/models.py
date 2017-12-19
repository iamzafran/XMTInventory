from django.db import models


# Create your models here.


class Department(models.Model):
    departmentName = models.CharField(max_length=250)


class Staff(models.Model):
    staffID = models.CharField(max_length=20, null=True, default=None, blank=True)
    staffName = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Tenant(models.Model):
    tenantName = models.CharField(max_length=250)


class Project(models.Model):
    projectName = models.CharField(max_length=250)








