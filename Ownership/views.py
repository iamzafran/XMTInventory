from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from .models import XMTStaff, Tenant, Customer, Department, TenantLocation, TenantPersonIncharge, Developers, \
    CustomerLocation, CustomerPersonInCharge
from Inventory.models import Computer, System, Email, Server, Projector, DataCenter, Software
# Create your views here.


@login_required(login_url='/login/')
def index(request):
    template = loader.get_template('staff/staff.html')
    staffs = XMTStaff.objects.all()
    context = {
        'staffs': staffs,
    }
    print(staffs)
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def tenant_view(request):
    template = loader.get_template('tenant/tenant.html')
    tenants = Tenant.objects.all()
    context = {
        "tenants": tenants
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def project_view(request):
    template = loader.get_template('customer/customer.html')
    customers = Customer.objects.all()
    context = {
        "customers": customers
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def department_view(request):
    template = loader.get_template('department/department.html')
    departments = Department.objects.all()
    context = {
        "departments": departments
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def tenant_detail(request, tenant_id):
    template = loader.get_template('tenant/tenantDetail.html')
    tenant = Tenant.objects.get(pk=tenant_id)

    try:
        tenantloc = TenantLocation.objects.filter(tenant=tenant)
    except ObjectDoesNotExist:
        tenantloc = None

    # try:
    #     computer = Computer.objects.filter(location=tenantloc)
    # except ObjectDoesNotExist:
    #     computer = None

    context = {
        "tenant": tenant,
        "locations": tenantloc
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def customer_detail(request, project_id):
    template = loader.get_template('customer/customerDetail.html')
    customer = Customer.objects.get(pk=project_id)

    try:
        customerlocation = CustomerLocation.objects.filter(customer=customer)
    except ObjectDoesNotExist:
        customerlocation = None

    context = {
        "customer": customer,
        "locations": customerlocation
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def tenant_location_detail(request, location_id):
    template = loader.get_template('location/locationLeasing.html')
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


@login_required(login_url='/login/')
def customer_location_detail(request, location_id):
    template = loader.get_template('customerlocation/locationLeasing.html')
    location = CustomerLocation.objects.get(pk=location_id)
    pic = CustomerPersonInCharge.objects.get(location=location)

    try:
        computers = Computer.objects.filter(customerLocation=location)

    except ObjectDoesNotExist:
        computers = None

    try:
        servers = Server.objects.filter(customerLocation=location)
    except ObjectDoesNotExist:
        servers = None

    try:
        projectors = Projector.objects.filter(customerLocation=location)
    except ObjectDoesNotExist:
        projectors = None

    print(computers)

    context = {
        "location": location,
        "computers": computers,
        "servers": servers,
        "projectors": projectors,
        "pic": pic
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def tenant_location_rental(request, location_id):
    template = loader.get_template('location/locationDCRental.html')
    location = TenantLocation.objects.get(pk=location_id)
    pic = TenantPersonIncharge.objects.get(location=location)
    datacenter = DataCenter.objects.filter(tenantlocation=location)

    context = {
        "location": location,
        "datacenter": datacenter,
        "pic": pic
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def customer_location_rental(request, location_id):
    template = loader.get_template('customerlocation/locationDCRental.html')
    location = CustomerLocation.objects.get(pk=location_id)
    pic = CustomerPersonInCharge.objects.get(location=location)
    datacenter = DataCenter.objects.filter(customerLocation=location)

    context = {
        "location": location,
        "datacenter": datacenter,
        "pic": pic
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def tenant_system_and_apps(request, location_id):
    template = loader.get_template('location/locationSystemAndApps.html')
    location = TenantLocation.objects.get(pk=location_id)
    pic = TenantPersonIncharge.objects.get(location=location)
    systems = System.objects.filter(tenantlocation=location)
    softwares = Software.objects.filter(tenantlocation=location)
    print(softwares)
    print(systems)
    context = {
        "location": location,
        "systems": systems,
        "softwares": softwares,
        "pic": pic
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def customer_system_and_apps(request, location_id):
    template = loader.get_template('customerlocation/locationSystemAndApps.html')
    location = CustomerLocation.objects.get(pk=location_id)
    pic = CustomerPersonInCharge.objects.get(location=location)
    systems = System.objects.filter(customerLocation=location)
    softwares = Software.objects.filter(customerLocation=location)
    print(softwares)
    print(systems)
    context = {
        "location": location,
        "systems": systems,
        "softwares": softwares,
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


class UpdateCustomerLocationInventory(APIView):
    def post(self, request):
        data = request.data
        customer_location_id = data["location"]
        computers = data["computers"]
        customerLocation = CustomerLocation.objects.get(id=customer_location_id)
        for c in computers:
            tagNo = c["pcTagNo"]
            startDate = c["startDate"]
            endDate = c["endDate"]
            computer = Computer.objects.get(pcTagNo=tagNo)
            computer.customerLocation = customerLocation
            computer.startDate = startDate
            computer.endDate = endDate
            computer.save()
        return HttpResponse("customer")


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


class UpdateCustomerServer(APIView):

    def post(self, request):
        data = request.data
        location_id = data["location"]
        servers = data["servers"]
        customerlocation = CustomerLocation.objects.get(pk=location_id)

        for s in servers:
            tagNumber = s["server"]
            startDate = s["startDate"]
            endDate = s["endDate"]
            update_server = Server.objects.get(tagNumber=tagNumber)
            update_server.customerLocation = customerlocation
            update_server.startDate = startDate
            update_server.endDate = endDate
            update_server.save()

        return HttpResponse("customer servers updated")


class DeleteTenantServer(APIView):

    def post(self, request):
        data = request.data
        tag = data["server"]

        delete_server = Server.objects.get(tagNumber=tag)
        delete_server.tenantlocation = None
        delete_server.save()
        return HttpResponse("Deleted Server")


class DeleteCustomerServer(APIView):

    def post(self, request):
        data = request.data
        tag = data["server"]

        delete_server = Server.objects.get(tagNumber=tag)
        delete_server.customerLocation = None
        delete_server.save()
        return HttpResponse("Deleted Customer Server")


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


class UpdateCustomerProjector(APIView):

    def post(self, request):
        data = request.data
        location_id = data["location"]
        projectors = data["projectors"]
        customerlocation = CustomerLocation.objects.get(pk=location_id)

        for p in projectors:
            tagNumber = p["projector"]
            startDate = p["startDate"]
            endDate = p["endDate"]
            update_projector = Projector.objects.get(projectorTag=tagNumber)
            update_projector.customerLocation = customerlocation
            update_projector.startDate = startDate
            update_projector.endDate = endDate
            update_projector.save()

        return HttpResponse("customer projector updated")


class DeleteTenantProjector(APIView):

    def post(self, request):
        data = request.data
        tag = data["projector"]

        delete_projector = Projector.objects.get(projectorTag=tag)
        delete_projector.tenantlocation = None
        delete_projector.save()
        return HttpResponse("Deleted projector")


class DeleteCustomerProjector(APIView):

    def post(self, request):
        data = request.data
        tag = data["projector"]

        delete_projector = Projector.objects.get(projectorTag=tag)
        delete_projector.customerLocation = None
        delete_projector.save()
        return HttpResponse("Deleted customer projector")



class DeleteTenantLocationInventory(APIView):

    def post(self, request):
        data = request.data
        computer = data["computer"]

        computer = Computer.objects.get(pcTagNo=computer)
        computer.tenantlocation = None
        computer.save()
        return HttpResponse("deleted")


class DeleteCustomerLocationInventory(APIView):

    def post(self, request):
        data = request.data
        computer = data["computer"]
        computer = Computer.objects.get(pcTagNo=computer)
        computer.customerLocation = None
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


class UpdateTenantDataCenter(APIView):

    def post(self, request):
        data = request.data
        location_id = data["location"]
        dc = data["dc"]
        tenantlocation = TenantLocation.objects.get(id=location_id)
        print(dc)
        for d in dc:
            print(d)
            rental_id = d["rental_id"]
            dataCenter = d["dc_location"]
            numberOfRacks = d["number_of_racks"]
            startDate = d["startDate"]
            endDate = d["endDate"]
            try:
                #check if rental_id exists
                dc = DataCenter.objects.get(pk=rental_id)
                dc.dataCenter = dataCenter
                dc.numberOfRacks = numberOfRacks
                dc.startDate = startDate
                dc.endDate = endDate
                dc.save()
            except ObjectDoesNotExist:
                #if does not exist create new rental
                dc = DataCenter(dataCenter=dataCenter, numberOfRacks=numberOfRacks, startDate=startDate, endDate=endDate,
                                tenantlocation=tenantlocation)
                dc.save()
        return HttpResponse("dc updated")


class DeleteTenantDataCenter(APIView):

    def post(self, request):
        data = request.data
        rental_id = data["rental_id"]
        rental = DataCenter.objects.get(pk=rental_id)
        rental.delete()
        return HttpResponse("rental deleted")


class UpdateCustomerDataCenter(APIView):

    def post(self, request):
        data = request.data
        location_id = data["location"]
        dc = data["dc"]
        customerlocation = CustomerLocation.objects.get(id=location_id)
        print(dc)
        for d in dc:
            print(d)
            rental_id = d["rental_id"]
            dataCenter = d["dc_location"]
            numberOfRacks = d["number_of_racks"]
            startDate = d["startDate"]
            endDate = d["endDate"]
            try:
                # check if rental_id exists
                dc = DataCenter.objects.get(pk=rental_id)
                dc.dataCenter = dataCenter
                dc.numberOfRacks = numberOfRacks
                dc.startDate = startDate
                dc.endDate = endDate
                dc.save()
            except ObjectDoesNotExist:
                # if does not exist create new rental
                dc = DataCenter(dataCenter=dataCenter, numberOfRacks=numberOfRacks, startDate=startDate,
                                endDate=endDate,
                                customerLocation=customerlocation)
                dc.save()
        return HttpResponse("dc customer updated")


class DeleteCustomerDataCenter(APIView):

    def post(self, request):
        data = request.data
        rental_id = data["rental_id"]
        rental = DataCenter.objects.get(pk=rental_id)
        rental.delete()
        return HttpResponse("rental customer deleted")


class AddSystemForTenant(APIView):

    def post(self, request):
        data = request.data
        location_id = data["location_id"]
        system_name = data["name"]
        developer_name = data["developer_name"]
        developer_contact = data["developer_contact"]
        start_date = data["startDate"]
        end_date = data["endDate"]
        db = data["db"]
        tenantlocation = TenantLocation.objects.get(id=location_id)

        system = System.objects.get(systemName=system_name)
        developer = Developers(developerName=developer_name, developerContact=developer_contact, startDate=start_date,
                               endDate=end_date, db=db)
        developer.save()
        system.developer = developer
        system.tenantlocation.add(tenantlocation)
        system.save()
        return HttpResponse("Added System")


class AddSystemForCustomer(APIView):

    def post(self, request):
        data = request.data
        location_id = data["location_id"]
        system_name = data["name"]
        developer_name = data["developer_name"]
        developer_contact = data["developer_contact"]
        start_date = data["startDate"]
        end_date = data["endDate"]
        db = data["db"]
        customerlocation = CustomerLocation.objects.get(id=location_id)

        system = System.objects.get(systemName=system_name)
        developer = Developers(developerName=developer_name, developerContact=developer_contact, startDate=start_date,
                               endDate=end_date, db=db)
        developer.save()
        system.developer = developer
        system.customerLocation.add(customerlocation)
        system.save()
        return HttpResponse("Added Customer System")


class AddSoftwareForTenant(APIView):

    def post(self, request):
        data = request.data
        location_id = data["location_id"]

        system_name = data["name"]
        developer_name = data["developer_name"]
        developer_contact = data["developer_contact"]
        start_date = data["startDate"]
        end_date = data["endDate"]
        db = data["db"]

        software = Software.objects.get(softwareName=system_name)
        developer = Developers(developerName=developer_name, developerContact=developer_contact, startDate=start_date,
                               endDate=end_date, db=db)
        tenantlocation = TenantLocation.objects.get(id=location_id)
        developer.save()
        software.developer = developer
        software.tenantlocation.add(tenantlocation)
        software.save()
        return HttpResponse("Added Software")


class AddSoftwareForCustomer(APIView):

    def post(self, request):
        data = request.data
        location_id = data["location_id"]

        system_name = data["name"]
        developer_name = data["developer_name"]
        developer_contact = data["developer_contact"]
        start_date = data["startDate"]
        end_date = data["endDate"]
        db = data["db"]

        software = Software.objects.get(softwareName=system_name)
        developer = Developers(developerName=developer_name, developerContact=developer_contact, startDate=start_date,
                               endDate=end_date, db=db)
        customerlocation = CustomerLocation.objects.get(id=location_id)
        developer.save()
        software.developer = developer
        software.customerLocation.add(customerlocation)
        software.save()
        return HttpResponse("Added Customer Software")


class UpdateSoftwareTenant(APIView):

    def post(self, request):
        data = request.data
        location = data["location_id"]
        software_id = data["software_id"]
        developer_id = data["developer_id"]
        developer_name = data["developer_name"]
        developer_contact = data["developer_contact"]
        startDate = data["startDate"]
        endDate = data["endDate"]
        db = data["db"]

        tenantlocation = TenantLocation.objects.get(pk=location)
        software = Software.objects.get(pk=software_id)
        developer = Developers.objects.get(pk=developer_id)
        developer.developerName = developer_name
        developer.developerContact = developer_contact
        developer.startDate = startDate
        developer.endDate = endDate
        developer.db = db
        developer.save()
        return HttpResponse("developer updated")


class UpdateSoftwareCustomer(APIView):

    def post(self, request):
        data = request.data
        location = data["location_id"]
        software_id = data["software_id"]
        developer_id = data["developer_id"]
        developer_name = data["developer_name"]
        developer_contact = data["developer_contact"]
        startDate = data["startDate"]
        endDate = data["endDate"]
        db = data["db"]

        tenantlocation = TenantLocation.objects.get(pk=location)
        software = Software.objects.get(pk=software_id)
        developer = Developers.objects.get(pk=developer_id)
        developer.developerName = developer_name
        developer.developerContact = developer_contact
        developer.startDate = startDate
        developer.endDate = endDate
        developer.db = db
        developer.save()
        return HttpResponse("developer customer updated")


class UpdateSystemTenant(APIView):

    def post(self, request):
        data = request.data
        location = data["location_id"]
        system_id = data["system_id"]
        developer_id = data["developer_id"]
        developer_name = data["developer_name"]
        developer_contact = data["developer_contact"]
        startDate = data["startDate"]
        endDate = data["endDate"]
        db = data["db"]

        tenantlocation = TenantLocation.objects.get(pk=location)
        system = System.objects.get(pk=system_id)
        developer = Developers.objects.get(pk=developer_id)
        developer.developerName = developer_name
        developer.developerContact = developer_contact
        developer.startDate = startDate
        developer.endDate = endDate
        developer.db = db
        developer.save()
        return HttpResponse("system developer updated")


class UpdateSystemCustomer(APIView):

    def post(self, request):
        data = request.data
        location = data["location_id"]
        system_id = data["system_id"]
        developer_id = data["developer_id"]
        developer_name = data["developer_name"]
        developer_contact = data["developer_contact"]
        startDate = data["startDate"]
        endDate = data["endDate"]
        db = data["db"]

        tenantlocation = TenantLocation.objects.get(pk=location)
        system = System.objects.get(pk=system_id)
        developer = Developers.objects.get(pk=developer_id)
        developer.developerName = developer_name
        developer.developerContact = developer_contact
        developer.startDate = startDate
        developer.endDate = endDate
        developer.db = db
        developer.save()
        return HttpResponse("system developer updated")


class DeleteTenantSystem(APIView):

    def post(self, request):
        data = request.data
        system = data["system_id"]
        location = data["location_id"]
        developer_id = data["developer_id"]

        system = System.objects.get(pk=system)
        tenantlocation = TenantLocation.objects.get(pk=location)
        developer = Developers.objects.get(pk=developer_id)
        system.tenantlocation.remove(tenantlocation)
        system.save()
        developer.delete()

        return HttpResponse("System Deleted")


class DeleteCustomerSystem(APIView):
    def post(self, request):
        data = request.data
        system = data["system_id"]
        location = data["location_id"]
        developer_id = data["developer_id"]

        system = System.objects.get(pk=system)
        customerlocation = CustomerLocation.objects.get(pk=location)
        developer = Developers.objects.get(pk=developer_id)
        system.customerLocation.remove(customerlocation)
        system.save()
        developer.delete()

        return HttpResponse("System Deleted")


class DeleteTenantSoftware(APIView):

    def post(self, request):
        data = request.data
        software_id = data["software_id"]
        location = data["location_id"]
        developer_id = data["developer_id"]

        software = Software.objects.get(pk=software_id)
        tenantlocation = TenantLocation.objects.get(pk=location)
        developer = Developers.objects.get(pk=developer_id)
        software.tenantlocation.remove(tenantlocation)
        software.save()
        developer.delete()

        return HttpResponse("Software Deleted")


class DeleteCustomerSoftware(APIView):

    def post(self, request):
        data = request.data
        software_id = data["software_id"]
        location = data["location_id"]
        developer_id = data["developer_id"]

        software = Software.objects.get(pk=software_id)
        customerlocation = CustomerLocation.objects.get(pk=location)
        developer = Developers.objects.get(pk=developer_id)
        software.customerLocation.remove(customerlocation)
        software.save()
        developer.delete()

        return HttpResponse("Software Customer Deleted")