from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Computer, Monitor, Projector, System, Email, DCAsset, Server, Software
from XMTInventory.serializers import ComputerSerializer, MonitorSerializer, ProjectorSerializer, \
    SystemSerializer, EmailSerializer, DCAssetSerializer, ServerSerializer, SoftwareSerializer
# Create your views here.


def index(request):
    template = loader.get_template('computer/computer.html')
    computers = Computer.objects.all()
    context = {
        'computers': computers,
    }
    return HttpResponse(template.render(context, request))


def projector(request):
    template = loader.get_template('projector/projector.html')
    projectors = Projector.objects.all()
    context = {
        'projectors': projectors,
    }
    return HttpResponse(template.render(context, request))


def monitor(request):
    template = loader.get_template('monitor/monitor.html')
    monitors = Monitor.objects.all()
    context = {
        'monitors': monitors,
    }
    return HttpResponse(template.render(context, request))


def system(request):
    template = loader.get_template('system/system.html')
    systems = System.objects.all()
    context = {
        'systems': systems
    }
    return HttpResponse(template.render(context, request))


def email(request):
    template = loader.get_template('email/email.html')
    emails = Email.objects.all()
    context = {
       'emails': emails
    }
    return HttpResponse(template.render(context, request))


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


def addNewProjector(request):
    template = loader.get_template('projector/addprojector.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


def addNewMonitor(request):
    template = loader.get_template('monitor/addmonitor.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


def addNewSystem(request):
    template = loader.get_template('system/addsystem.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


def addNewEmail(request):
    template = loader.get_template('email/addemail.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


def dcasset(request):
    template = loader.get_template('dcasset/dcasset.html')
    dcassets = DCAsset.objects.all()

    context = {
        'dcassets': dcassets,
    }
    return HttpResponse(template.render(context, request))


def addNewDCasset(request):
    template = loader.get_template('dcasset/addDCasset.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


def server(request):
    template = loader.get_template('server/server.html')
    servers = Server.objects.all()

    context = {
        'servers': servers
    }
    return HttpResponse(template.render(context, request))


def addServer(request):
    template = loader.get_template('server/addserver.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


def software(request):
    template = loader.get_template('software/software.html')
    softwares = Software.objects.all()

    context = {
        'softwares': softwares
    }
    return HttpResponse(template.render(context, request))


def addsoftware(request):
    template = loader.get_template('software/addsoftware.html')

    context = {
    }
    return HttpResponse(template.render(context, request))


class ComputerAutoComplete(APIView):

    def post(self, request):
        data = request.data
        print(request)
        search = data["search"]
        computers = Computer.objects.raw("SELECT * FROM Inventory_computer WHERE pcTagNo LIKE '" + search + "%'")
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
        operatingSystem = computer["os"]
        processor = computer["processor"]
        systemType = computer["systemType"]
        ram = computer["systemType"]
        hardDrive = computer["hdd"]

        c = Computer(pcModel=pcModel, pcTagNo=pcTagNo, pcModelSeries=pcModelSeries, pcName=pcName, serialNo=serialNo,
                     operatingSystem=operatingSystem, processor=processor,
                     systemType=systemType, ram=ram, hardDrive=hardDrive)

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
        serializer = ComputerSerializer(c, many=False)
        print(c.id)
        return Response(serializer.data)


class MonitorList(APIView):

    def get(self, request):
        monitors = Monitor.objects.all()
        serializer = MonitorSerializer(monitors, many=True)
        return Response(serializer.data)

    def post(self, request):

        monitor = request.data
        serialNumber = monitor["serialNo"]
        tagNumber = monitor["tagNo"]
        monitorAge= monitor["age"]

        m = Monitor(serialNo=serialNumber, tagNo=tagNumber, age=monitorAge)
        m.save()
        serialzer = MonitorSerializer(m, many=False)
        print(m.id)
        return Response(serialzer.data)


class ProjectorList(APIView):

    def get(self, request):
        projectors = Projector.objects.all()
        serializer = ProjectorSerializer(projectors, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        model = data["model"]
        year = data["year"]
        serial_number = data["serial_number"]
        tag = data["tag"]
        p = Projector(projectorModel=model, projectorYear=year, projectorSerialNumber=serial_number, projectorTag=tag)
        p.save()
        serializer = ProjectorSerializer(p, many=False)
        print(p.id)
        return Response(serializer.data)


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

        serializer = SystemSerializer(s, many=False)
        print(s.id)
        return Response(serializer.data)


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

        serializer = EmailSerializer(e, many=False)

        return Response(serializer.data)


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

        d = DCAsset(equipment=equipment, description=description, serialNumber=serial_number)

        d.save()

        serializer = DCAssetSerializer(d, many=False)

        return Response(serializer.data)


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

        s = Server(hostname=hostname, serverModel=server_model, ipv4=ip, domain=domain, username=username,
                   password=password, operatingSystem=os, serialNumber=serial_number, productKey=product_key,
                   processor=processor, hardDrive=hdd, application=application, location=location)

        s.save()

        serializer = ServerSerializer(s, many=False)

        return Response(serializer.data)


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

        serializer = SoftwareSerializer(s, many=False)

        return Response(serializer.data)
