from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from .models import XMTStaff
from Inventory.models import Computer, System, Email
# Create your views here.


def index(request):
    template = loader.get_template('staff/staff.html')
    staffs = XMTStaff.objects.all()
    context = {
        'staffs': staffs,
    }
    print(staffs)
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

