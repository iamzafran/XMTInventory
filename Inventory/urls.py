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
    url(r'^software/$', views.software, name='software'),
    url(r'^software/add$', views.addsoftware, name='addsoftware'),
    url(r'^computer/(?P<computer_id>[0-9]+)$', views.computer_detail, name='computer_detail'),
    url(r'^server/(?P<server_id>[0-9]+)$', views.server_detail, name='server_detail'),
    url(r'^projector/(?P<projector_id>[0-9]+)$', views.projector_detail, name='projector_detail'),
    url(r'^monitor/(?P<monitor_id>[0-9]+)$', views.monitor_detail, name='monitor_detail'),
    url(r'^dcasset/(?P<dc_asset_id>[0-9]+)$', views.dc_asset_detail, name='dc_asset_detail'),


]
