from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from .models import XMTStaff, Tenant, Project, Department
from Inventory.models import Computer, System, Email, Server
# Create your views here.


def index(request):
    template = loader.get_template('staff/staff.html')
    staffs = XMTStaff.objects.all()
    context = {
        'staffs': staffs,
    }
    print(staffs)
    return HttpResponse(template.render(context, request))


def tenant_view(request):
    template = loader.get_template('tenant/tenant.html')
    tenants = Tenant.objects.all()
    context = {
        "tenants": tenants
    }
    return HttpResponse(template.render(context, request))


def project_view(request):
    template = loader.get_template('project/project.html')
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return HttpResponse(template.render(context, request))


def department_view(request):
    template = loader.get_template('department/department.html')
    departments = Department.objects.all()
    context = {
        "departments": departments
    }
    return HttpResponse(template.render(context, request))


def staff_detail(request, staff_id):
    template = loader.get_template('staff/staffDetail.html')
    staff = XMTStaff.objects.get(pk=staff_id)
    computerquery = Computer.objects.raw("SELECT * FROM Inventory_computer WHERE xmtstaff_id="+staff_id)
    systemquery = System.objects.raw("SELECT * FROM Inventory_system WHERE xmtstaff_id="+staff_id)
    emailquery = Email.objects.raw("SELECT * FROM Inventory_email WHERE xmtstaff_id="+staff_id)
    computer = None
    system = None
    email = None
    for c in computerquery:
        computer = c

    for s in systemquery:
        system = s

    for e in emailquery:
        email = e

    context = {
        'staff': staff,
        'computer': computer,
        'system': system,
        'email': email,
    }
    print(computer)
    print(system)
    print(email)
    return HttpResponse(template.render(context, request))


def tenant_detail(request, tenant_id):
    template = loader.get_template('tenant/tenantDetail.html')
    tenant = Tenant.objects.get(pk=tenant_id)

    try:
        computer = Computer.objects.filter(tenant=tenant)
    except ObjectDoesNotExist:
        computer = None

    context = {
        "tenant": tenant,
        "computers": computer
    }
    return HttpResponse(template.render(context, request))


def project_detail(request, project_id):
    template = loader.get_template('project/projectDetail.html')
    project = Project.objects.get(pk=project_id)

    try:
        computer = Computer.objects.filter(project=project)
    except ObjectDoesNotExist:
        computer = None

    context = {
        "project": project,
        "computers": computer
    }
    return HttpResponse(template.render(context, request))


def department_detail(request, department_id):
    template = loader.get_template('department/departmentDetail.html')
    department = Department.objects.get(pk=department_id)

    try:
        servers = Server.objects.filter(department=department)
    except ObjectDoesNotExist:
        servers = None

    context = {
        "department": department,
        "servers": servers
    }
    return HttpResponse(template.render(context, request))


class UpdateStaffInventory(APIView):

    def post(self, request):
        update_data = request.data
        staffId = update_data["staff_id"]
        pcTagNo = update_data["pcTagNo"]
        systemName = update_data["systemName"]
        principalName = update_data["principalName"]

        staff = XMTStaff.objects.get(id=staffId)

        try:
            newPC = Computer.objects.get(pcTagNo=pcTagNo)
        except ObjectDoesNotExist:
            newPC = None

        try:
            newSystem = System.objects.get(systemName=systemName)
        except ObjectDoesNotExist:
            newSystem = None

        try:
            newEmail = Email.objects.get(principalName=principalName)
        except ObjectDoesNotExist:
            newEmail = None

        print(newPC)
        print(newSystem)
        print(newEmail)

        if newPC is not None:
            newPC.xmtstaff = staff
            newPC.save()

        if newSystem is not None:
            newSystem.xmtstaff = staff
            newSystem.save()

        if newEmail is not None:
            newEmail.xmtstaff = staff
            newEmail.save()

        return HttpResponse("True")


class UpdateTenantInventory(APIView):

    def post(self, request):
        data = request.data
        tenant_id = data["tenant"]
        computers = data["computers"]
        tenant = Tenant.objects.get(id=tenant_id)
        for c in computers:
            computer = Computer.objects.get(pcTagNo=c)
            computer.tenant = tenant
            computer.save()
        return HttpResponse("true")


class DeleteTenantInventory(APIView):

    def post(self, request):
        data = request.data
        computer = data["computer"]

        computer = Computer.objects.get(pcTagNo=computer)
        computer.tenant = None
        computer.save()
        return HttpResponse("deleted")


class UpdateProjectInventory(APIView):

    def post(self, request):
        data = request.data
        project_id = data["project"]
        computers = data["computers"]
        project = Project.objects.get(id=project_id)
        for c in computers:
            computer = Computer.objects.get(pcTagNo=c)
            computer.project = project
            computer.save()
        return HttpResponse("true")


class DeleteProjectInventory(APIView):

    def post(self, request):
        data = request.data
        computer = data["computer"]

        computer = Computer.objects.get(pcTagNo=computer)
        computer.project = None
        computer.save()
        return HttpResponse("deleted")


class UpdateDepartmentInventory(APIView):

    def post(self, request):
        data = request.data
        department_id = data["department"]
        servers = data["servers"]
        department = Department.objects.get(id=department_id)
        for s in servers:
            server = Server.objects.get(hostname=s)
            server.department = department
            server.save()
        return HttpResponse("true")


class DeleteDepartmentInventory(APIView):

    def post(self, request):
        data = request.data
        hostname = data["hostname"]

        server = Server.objects.get(hostname=hostname)
        server.department = None
        server.save()
        return HttpResponse("deleted")