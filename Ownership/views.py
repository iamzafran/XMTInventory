from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
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

