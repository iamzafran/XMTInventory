from django.contrib import admin
from .models import Staff, Project, Tenant, Department
# Register your models here.

admin.site.register(Staff)
admin.site.register(Project)
admin.site.register(Tenant)
admin.site.register(Department)