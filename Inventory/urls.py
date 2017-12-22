from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^projector/$', views.projector, name='projector'),
    url(r'^projector/add/$', views.addNewProjector, name='addprojector'),
    url(r'^computer/add/$', views.addNewComputer, name='addcomputer'),
    url(r'^computer/$', views.index, name='computer'),
    url(r'^monitor/$', views.monitor, name='monitor'),
    url(r'^monitor/add$', views.addNewMonitor, name='monitor'),
    url(r'^system/$', views.system, name='monitor'),
    url(r'^system/add$', views.addNewSystem, name='monitor'),
    url(r'^email/$', views.email, name='monitor'),
    url(r'^email/add$', views.addNewEmail, name='monitor'),
    url(r'^dcasset/$', views.dcasset, name='dcasset'),
    url(r'^dcasset/add$', views.addNewDCasset, name='adddcasset'),
    url(r'^server/$', views.server, name='server'),
    url(r'^server/add$', views.addServer, name='addserver'),

]
