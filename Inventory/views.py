from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Computer, Monitor, Projector
from XMTInventory.serializers import ComputerSerializer, MonitorSerializer, ProjectorSerializer
# Create your views here.


def index(request):
    template = loader.get_template('computer/computer.html')
    context = {}
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

        if pcModel == 1:

            if computer["projector"] is not None:
                projector = Projector.objects.get(pk=computer["projector"])
                c.projector = projector

            if computer["monitor"] is not None:
                monitor = Monitor.objects.get(pk=computer["monitor"])
                c.monitor = monitor

        else:
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
        projector = request.data
        model = projector["model"]
        year = projector["year"]
        serial_number = projector["serial_number"]
        tag = projector["tag"]
        p = Projector(projectorModel=model, projectorYear=year, projectorSerialNumber=serial_number, projectorTag=tag)
        p.save()
        serializer = ProjectorSerializer(p, many=False)
        print(p.id)
        return Response(serializer.data)


