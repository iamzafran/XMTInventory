from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from .models import XMTStaff, Tenant, Customer, Department, TenantLocation, TenantPersonIncharge
from Inventory.models import Computer, System, Email, Server, Projector
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
    template = loader.get_template('customer/customer.html')
    customers = Customer.objects.all()
    context = {
        "customers": customers
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
        tenantloc = TenantLocation.objects.filter(tenant=tenant)
    except ObjectDoesNotExist:
        tenantloc = None

    # try:
    #     computer = Computer.objects.filter(tenantlocation=tenantloc)
    # except ObjectDoesNotExist:
    #     computer = None

    context = {
        "tenant": tenant,
        "locations": tenantloc
    }
    return HttpResponse(template.render(context, request))


def project_detail(request, project_id):
    template = loader.get_template('customer/customerDetail.html')
    project = Customer.objects.get(pk=project_id)

    try:
        computer = Computer.objects.filter(project=project)
    except ObjectDoesNotExist:
        computer = None

    context = {
        "customer": project,
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


def department_location_detail(request, location_id):
    template = loader.get_template('tenantlocation/tenantLocationLeasing.html')
    location = TenantLocation.objects.get(pk=location_id)
    pic = TenantPersonIncharge.objects.get(location=location)

    try:
        computers = Computer.objects.filter(tenantlocation=location)

    except ObjectDoesNotExist:
        computers = None

    try:
        servers = Server.objects.filter(tenantlocation=location)
    except ObjectDoesNotExist:
        servers = None

    try:
        projectors = Projector.objects.filter(tenantlocation=location)
    except ObjectDoesNotExist:
        projectors = None

    context = {
        "location": location,
        "computers": computers,
        "servers": servers,
        "projectors": projectors,
        "pic": pic
    }
    return HttpResponse(template.render(context, request))


class StaffAutoComplete(APIView):

    def post(self, request):
        data = request.data
        print(request)
        search = data["search"]
        staffs = XMTStaff.objects.filter(staffName__icontains=search)
        response = []

        for s in staffs:
            i = {
                'label': s.staffName
            }
            response.append(i)
        return JsonResponse(response, safe=False)


class ProjectAutoComplete(APIView):

    def post(self, request):
        data = request.data
        print(request)
        search = data["search"]
        projects = Customer.objects.filter(projectName__icontains=search)
        response = []

        for p in projects:
            i = {
                'label': p.projectName
            }
            response.append(i)
        return JsonResponse(response, safe=False)


class TenantAutoComplete(APIView):

    def post(self, request):
        data = request.data
        print(request)
        search = data["search"]
        tenants = Tenant.objects.filter(tenantName__icontains=search)
        response = []

        for t in tenants:
            i = {
                'label': t.tenantName
            }
            response.append(i)
        return JsonResponse(response, safe=False)


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


class UpdateTenantLocationInventory(APIView):

    def post(self, request):
        data = request.data
        tenant_location_id = data["location"]
        computers = data["computers"]
        tenantLocation = TenantLocation.objects.get(id=tenant_location_id)
        for c in computers:
            tagNo = c["pcTagNo"]
            startDate = c["startDate"]
            endDate = c["endDate"]
            computer = Computer.objects.get(pcTagNo=tagNo)
            computer.tenantlocation = tenantLocation
            computer.startDate = startDate
            computer.endDate = endDate
            computer.save()
        return HttpResponse("true")


class UpdateTenantServer(APIView):
    def post(self, request):
        data = request.data
        location_id = data["location"]
        servers = data["servers"]
        tenantlocation = TenantLocation.objects.get(pk=location_id)

        for s in servers:
            tagNumber = s["server"]
            startDate = s["startDate"]
            endDate = s["endDate"]
            update_server = Server.objects.get(tagNumber=tagNumber)
            update_server.tenantlocation = tenantlocation
            update_server.startDate = startDate
            update_server.endDate = endDate
            update_server.save()

        return HttpResponse("servers updated")


class DeleteTenantServer(APIView):

    def post(self, request):
        data = request.data
        tag = data["server"]

        delete_server = Server.objects.get(tagNumber=tag)
        delete_server.tenantlocation = None
        delete_server.save()
        return HttpResponse("Deleted Server")


class UpdateTenantProjector(APIView):

    def post(self, request):
        data = request.data
        location_id = data["location"]
        projectors = data["projectors"]
        tenantlocation = TenantLocation.objects.get(pk=location_id)

        for p in projectors:
            tagNumber = p["projector"]
            startDate = p["startDate"]
            endDate = p["endDate"]
            update_projector = Projector.objects.get(projectorTag=tagNumber)
            update_projector.tenantlocation = tenantlocation
            update_projector.startDate = startDate
            update_projector.endDate = endDate
            update_projector.save()

        return HttpResponse("projector updated")


class DeleteTenantProjector(APIView):

    def post(self, request):
        data = request.data
        tag = data["projector"]

        delete_projector = Projector.objects.get(projectorTag=tag)
        delete_projector.tenantlocation = None
        delete_projector.save()
        return HttpResponse("Deleted projector")


class DeleteTenantLocationInventory(APIView):

    def post(self, request):
        data = request.data
        computer = data["computer"]

        computer = Computer.objects.get(pcTagNo=computer)
        computer.tenantlocation = None
        computer.save()
        return HttpResponse("deleted")


class UpdateProjectInventory(APIView):

    def post(self, request):
        data = request.data
        project_id = data["customer"]
        computers = data["computers"]
        project = Customer.objects.get(id=project_id)
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







