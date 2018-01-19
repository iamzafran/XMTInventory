from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Computer, Monitor, Projector, System, Email, DCAsset, Server, Software
from Inventory.models import TenantLocation, XMTStaff, Customer
from XMTInventory.serializers import ComputerSerializer, MonitorSerializer, ProjectorSerializer, \
    SystemSerializer, EmailSerializer, DCAssetSerializer, ServerSerializer, SoftwareSerializer
# Create your views here.


def login_user(request):
    email_login = request.POST['email']
    password = request.POST['password']
    print(email_login)
    print(password)
    user = authenticate(email=email_login, password=password)
    if user is not None:
        if user.is_active:
            print("ok")
            login(request, user)
            return HttpResponseRedirect("/")

        else:
            print("not active")

            return HttpResponseRedirect("/login/")
    else:
        print("not user")

        return HttpResponseRedirect("/login/")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/login/")


@login_required(login_url='/login/')
def index(request):
    template = loader.get_template('computer/computer.html')
    computers = Computer.objects.all()
    context = {
        'computers': computers,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def projector(request):
    template = loader.get_template('projector/projector.html')
    projectors = Projector.objects.all()
    context = {
        'projectors': projectors,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def monitor(request):
    template = loader.get_template('monitor/monitor.html')
    monitors = Monitor.objects.all()
    context = {
        'monitors': monitors,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def system(request):
    template = loader.get_template('system/system.html')
    systems = System.objects.all()
    context = {
        'systems': systems
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def email(request):
    template = loader.get_template('email/email.html')
    emails = Email.objects.all()
    context = {
       'emails': emails
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def addNewComputer(request):
    template = loader.get_template('computer/addcomputer.html')
    monitors = Monitor.objects.raw('SELECT * FROM Inventory_monitor')
    projectors = Projector.objects.raw('SELECT * FROM Inventory_projector')
    for p in projectors:
        print(p.projectorTag)
    context = {
        'monitors': monitors,
        'projectors': projectors,

    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def addNewProjector(request):
    template = loader.get_template('projector/addprojector.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def addNewMonitor(request):
    template = loader.get_template('monitor/addmonitor.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def addNewSystem(request):
    template = loader.get_template('system/addsystem.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def addNewEmail(request):
    template = loader.get_template('email/addemail.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def dcasset(request):
    template = loader.get_template('dcasset/dcasset.html')
    dcassets = DCAsset.objects.all()

    context = {
        'dcassets': dcassets,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def addNewDCasset(request):
    template = loader.get_template('dcasset/addDCasset.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def server(request):
    template = loader.get_template('server/server.html')
    servers = Server.objects.all()

    context = {
        'servers': servers
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def addServer(request):
    template = loader.get_template('server/addserver.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def software(request):
    template = loader.get_template('software/software.html')
    softwares = Software.objects.all()

    context = {
        'softwares': softwares
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def addsoftware(request):
    template = loader.get_template('software/addsoftware.html')

    context = {
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def computer_detail(request, computer_id):
    template = loader.get_template('computer/computerDetail.html')
    computer = Computer.objects.get(pk=computer_id)
    context = {
        "computer": computer,
        "projector": computer.projector,
        "monitor": computer.monitor
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def server_detail(request, server_id):
    template = loader.get_template('server/serverDetail.html')
    s = Server.objects.get(pk=server_id)
    context = {
        "server": s
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def projector_detail(request, projector_id):
    template = loader.get_template('projector/projectorDetail.html')
    p = Projector.objects.get(pk=projector_id)
    context = {
        "projector": p
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def monitor_detail(request, monitor_id):
    template = loader.get_template('monitor/monitorDetail.html')
    m = Monitor.objects.get(pk=monitor_id)
    context = {
        "monitor": m
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def dc_asset_detail(request, dc_asset_id):
    template = loader.get_template('dcasset/dcassetDetail.html')
    d = DCAsset.objects.get(pk=dc_asset_id)
    context = {
        "asset": d
    }
    return HttpResponse(template.render(context, request))


class ComputerAutoComplete(APIView):

    def post(self, request):
        data = request.data
        print(request)
        search = data["search"]
        computers = Computer.objects.filter(pcTagNo__icontains=search, tenantlocation=None, xmtstaff=None,
                                            customerLocation=None)
        response = []

        for c in computers:
            computer = {
                'label': c.pcTagNo
            }
            response.append(computer)
        return JsonResponse(response, safe=False)


class ComputerList(APIView):

    def get(self, request):
        computers = Computer.objects.all()
        serializer = ComputerSerializer(computers, many=True)
        return Response(serializer.data)

    def post(self, request):
        computer = request.data
        pcModel = computer["model"]
        pcTagNo = computer["tag"]
        pcModelSeries = computer["model_series"]
        pcName = computer["name"]
        serialNo = computer["serial_number"]
        yearOfPurhcase = computer["year_of_purchase"]
        startLease = computer["start_lease"]
        endLease = computer["end_lease"]
        warrantyPeriod = computer["warranty_period"]
        extendedWarranty = computer["extended_warranty"]
        operatingSystem = computer["os"]
        processor = computer["processor"]
        systemType = computer["systemType"]
        ram = computer["ram"]
        hardDrive = computer["hdd"]

        c = Computer(pcModel=pcModel, pcTagNo=pcTagNo, pcModelSeries=pcModelSeries, pcName=pcName, serialNo=serialNo,
                     yearOfPurchase=yearOfPurhcase, startLeasing=startLease, endLeasing=endLease,
                     warrantyPeriod=warrantyPeriod, extendedWarranty=extendedWarranty, operatingSystem=operatingSystem,
                     processor=processor, systemType=systemType, ram=ram, hardDrive=hardDrive)

        print("PC model = "+pcModel)

        if pcModel == "1":
            print("Desktop computer")
            if computer["projector"] is not None:
                projector = Projector.objects.get(pk=computer["projector"])
                c.projector = projector

            if computer["monitor"] is not None:
                print(computer["monitor"])
                monitor = Monitor.objects.get(pk=computer["monitor"])
                c.monitor = monitor

        else:
            print("Not Desktop computer")

            if computer["projector"] is not None:
                projector = Projector.objects.get(pk=computer["projector"])
                c.projector = projector

        c.save()
        return HttpResponse(c.serialNo)


class ComputerUpdate(APIView):

    def post(self, request):
        data = request.data
        id = data["id"]
        new_monitor = data["monitor"]
        os = data["os"]
        pcName = data["pcName"]
        new_projector = data["projector"]
        remarks = data["remarks"]
        startLeasing = data["start_leasing"]
        endLeasing = data["end_leasing"]
        warrantyPeriod = data["warranty_period"]
        extendedWarranty = data["extended_warranty"]

        computer = Computer.objects.get(pk=id)
        print(startLeasing)
        print(endLeasing)
        print(warrantyPeriod)
        print(extendedWarranty)
        if new_monitor:
            m = Monitor.objects.get(tagNo=new_monitor)
            computer.monitor = m

        if new_projector:
            p = Projector.objects.get(projectorTag=new_projector)
            computer.projector = p

        computer.operatingSystem = os
        computer.pcName = pcName
        computer.remarks = remarks
        computer.startLeasing = startLeasing
        computer.endLeasing = endLeasing
        computer.warrantyPeriod = warrantyPeriod
        computer.extendedWarranty = extendedWarranty

        computer.save()
        return HttpResponse(computer.serialNo);


class ServerUpdate(APIView):

    def post(self, request):
        data = request.data
        serverID = data["id"]
        application = data["application"]
        domain = data["domain"]
        end_leasing = data["end_leasing"]
        extended_warranty = data["extended_warranty"]
        hostname = data["hostname"]
        ipv4 = data["ipv4"]
        os = data["os"]
        password = data["password"]
        start_leasing = data["start_leasing"]
        username = data["username"]
        warranty_period = data["warranty_period"]

        s = Server.objects.get(pk=serverID)
        s.application = application
        s.domain = domain
        s.endLeasing = end_leasing
        s.startLeasing = start_leasing
        s.warrantyPeriod = warranty_period
        s.extendedWarranty = extended_warranty
        s.hostname = hostname
        s.ipv4 = ipv4
        s.operatingSystem = os
        s.username = username
        s.password = password
        s.save()

        return HttpResponse(s.serialNumber)


class UpdateComputerOwnership(APIView):

    def post(self, request):
        data = request.data
        ownership_type = data["type"]
        computer_id = data["computer_id"]
        project = data["project_name"]
        tenant = data["tenant_name"]
        staff = data["staff_name"]

        computer = Computer.objects.get(pk=computer_id)
        computer.tenant = None
        computer.xmtstaff = None
        computer.project = None

        if ownership_type == "staff":
            staff = XMTStaff.objects.get(staffName=staff)
            computer.xmtstaff = staff
        elif ownership_type == "customer":
            project = Customer.objects.get(projectName=project)
            computer.project = project
        elif ownership_type == "tenant":
            tenant = Tenant.objects.get(tenantName=tenant)
            computer.tenant = tenant

        computer.save()

        return HttpResponse("Updated")


class MonitorList(APIView):

    def get(self, request):
        monitors = Monitor.objects.all()
        serializer = MonitorSerializer(monitors, many=True)
        return Response(serializer.data)

    def post(self, request):

        data = request.data
        serialNumber = data["serialNo"]
        tagNumber = data["tagNo"]
        year = data["year_of_purchase"]
        start_leasing = data["start_leasing"]
        end_leasing = data["end_leasing"]
        warranty_period = data["warranty_period"]
        extended_warranty = data["extended_warranty"]

        m = Monitor(serialNo=serialNumber, tagNo=tagNumber, yearOfPurchase=year, startLeasing=start_leasing,
                    endLeasing=end_leasing, warrantyPeriod=warranty_period, extendedWarranty=extended_warranty)
        m.save()

        return HttpResponse(m.serialNo)


class MonitorAutoComplete(APIView):

    def post(self, request):
        data = request.data
        print(request)
        search = data["search"]
        monitors = Monitor.objects.filter(tagNo__icontains=search)
        response = []

        for m in monitors:
            i = {
                'label': m.tagNo
            }
            response.append(i)
        return JsonResponse(response, safe=False)


class MonitorUpdate(APIView):

    def post(self, request):
        data = request.data
        monitor_id = data["id"]
        start_leasing = data["start_leasing"]
        end_leasing = data["end_leasing"]
        warranty_period = data["warranty_period"]
        extended_warranty = data["extended_warranty"]

        m = Monitor.objects.get(pk=monitor_id)
        m.startLeasing = start_leasing
        m.endLeasing = end_leasing
        m.warrantyPeriod = warranty_period
        m.extendedWarranty = extended_warranty

        m.save()

        return HttpResponse(m.serialNo)


class ProjectorList(APIView):

    def get(self, request):
        projectors = Projector.objects.all()
        serializer = ProjectorSerializer(projectors, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        model = data["model"]
        year = data["year_of_purchase"]
        start_leasing = data["start_leasing"]
        end_leasing = data["end_leasing"]
        warranty_period = data["warranty_period"]
        extended_warranty = data["extended_warranty"]
        serial_number = data["serial_number"]
        tag = data["tag"]
        p = Projector(projectorModel=model, projectorSerialNumber=serial_number, projectorTag=tag,
                      yearOfPurchase=year, startLeasing=start_leasing, endLeasing=end_leasing,
                      warrantyPeriod=warranty_period, extendedWarranty=extended_warranty)
        p.save()

        return HttpResponse(p.projectorSerialNumber)


class ProjectorAutoComplete(APIView):

    def post(self, request):
        data = request.data
        print(request)
        search = data["search"]
        projectors = Projector.objects.filter(projectorTag__icontains=search)
        response = []

        for p in projectors:
            i = {
                'label': p.projectorTag
            }
            response.append(i)
        return JsonResponse(response, safe=False)


class ProjectorUpdate(APIView):

    def post(self, request):
        data = request.data
        end_leasing = data["end_leasing"]
        extended_warranty = data["extended_warranty"]
        projector_id = data["id"]
        start_leasing = data["start_leasing"]
        warranty_period = data["warranty_period"]

        p = Projector.objects.get(pk=projector_id)
        p.endLeasing = end_leasing
        p.extendedWarranty = extended_warranty
        p.startLeasing = start_leasing
        p.warrantyPeriod = warranty_period
        p.save()

        return HttpResponse(p.projectorSerialNumber)


class SystemList(APIView):

    def get(self, request):
        s = System.objects.all()
        serializer = SystemSerializer(s, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        system_name = data["system_name"]
        location = data["location"]

        s = System(systemName=system_name, location=location)
        s.save()
        return HttpResponse(s.systemName)


class SystemAutoComplete(APIView):

    def post(self, request):
        data = request.data
        print(request)
        search = data["search"]
        system_query = System.objects.raw("SELECT * FROM Inventory_system WHERE systemName LIKE '" + search + "%'")
        response = []

        for s in system_query:
            row = {
                'label': s.systemName
            }
            response.append(row)
        return JsonResponse(response, safe=False)


class SoftwareAutoComplete(APIView):

    def post(self, request):
        data = request.data
        print(request)
        search = data["search"]
        softwares = Software.objects.filter(softwareName__icontains=search)

        response = []
        for s in softwares:
            row = {
                'label': s.softwareName
            }
            response.append(row)
        return JsonResponse(response, safe=False)


class EmailList(APIView):

    def get(self, request):
        e = Email.objects.all()
        seralizer = EmailSerializer(e, many=True)
        return Response(seralizer.data)

    def post(self, request):
        data = request.data
        licenses = data["licenses"]
        principal_name = data["principal_name"]
        date_created = data["date_created"]

        e = Email(licenses=licenses, principalName=principal_name, dateCreated=date_created)
        e.save()

        return HttpResponse(e.principalName)


class EmailListAutoComplete(APIView):

    def post(self, request):
        data = request.data
        print(request)
        search = data["search"]
        email_query = Email.objects.raw("SELECT * FROM Inventory_email WHERE principalName LIKE '" + search + "%'")
        response = []

        for e in email_query:
            row = {
                'label': e.principalName
            }
            response.append(row)
        return JsonResponse(response, safe=False)


class DCAssetList(APIView):

    def get(self, request):
        d = DCAsset.objects.all()
        serializer = DCAssetSerializer(d, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        equipment = data["equipment"]
        description = data["description"]
        serial_number = data["serial_number"]
        year = data["year_of_purchase"]
        start_leasing = data["start_lease"]
        end_leasing = data["end_lease"]
        warranty_period = data["warranty_period"]
        extended_warranty = data["extended_warranty"]

        d = DCAsset(equipment=equipment, description=description, serialNumber=serial_number, yearOfPurchase=year,
                    startLeasing=start_leasing, endLeasing=end_leasing, warrantyPeriod=warranty_period,
                    extendedWarranty=extended_warranty)

        d.save()

        return HttpResponse(d.serialNumber)


class DCAssetUpdate(APIView):

    def post(self, request):
        data = request.data
        end_leasing = data["end_leasing"]
        extended_warranty = data["extended_warranty"]
        dc_asset_id = data["id"]
        start_leasing = data["start_leasing"]
        warranty_period = data["warranty_period"]

        dc = DCAsset.objects.get(pk=dc_asset_id)
        dc.startLeasing = start_leasing
        dc.endLeasing = end_leasing
        dc.warrantyPeriod = warranty_period
        dc.extendedWarranty = extended_warranty
        dc.save()
        return HttpResponse(dc.serialNumber)


class ServerList(APIView):

    def get(self, request):
        s = Server.objects.all()
        serializer = ServerSerializer(s, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        hostname =  data["hostname"]
        server_model = data["server_model"]
        ip = data["ip"]
        domain = data["domain"]
        username = data["username"]
        password = data["password"]
        os = data["os"]
        serial_number = data["serial_number"]
        product_key = data["product_key"]
        processor = data["processor"]
        hdd = data["hdd"]
        application = data["application"]
        location = data["location"]
        end_lease = data["end_lease"]
        extended_warranty = data["extended_warranty"]
        start_lease = data["start_lease"]
        warranty_period = data["warranty_period"]
        year_of_purchase = data["year_of_purchase"]

        s = Server(hostname=hostname, serverModel=server_model, yearOfPurchase=year_of_purchase, startLeasing=start_lease,
                   warrantyPeriod=warranty_period, endLeasing=end_lease, extendedWarranty=extended_warranty, ipv4=ip,
                   domain=domain, username=username, password=password, operatingSystem=os, serialNumber=serial_number, productKey=product_key,
                   processor=processor, hardDrive=hdd, application=application, location=location)

        s.save()

        return HttpResponse(s.serialNumber)


class ServerAutoComplete(APIView):

    def post(self, request):
        data = request.data
        print(request)
        search = data["search"]
        servers = Server.objects.filter(tagNumber__icontains=search, department=None)
        response = []

        for s in servers:
            computer = {
                'label': s.tagNumber
            }
            response.append(computer)
        return JsonResponse(response, safe=False)


class SoftwareList(APIView):

    def get(self, request):
        s = Software.objects.all()
        serializer = SoftwareSerializer(s, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        software_name = data["software_name"]

        s = Software(softwareName=software_name)
        s.save()

        return HttpResponse(s.softwareName)
