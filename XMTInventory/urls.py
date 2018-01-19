"""XMTInventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from Inventory import views as iviews
from Ownership import views as oviews
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', iviews.index, name='index'),
    url(r'^inventory/', include('Inventory.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/monitors/add', iviews.MonitorList.as_view()),
    url(r'^api/projectors/add', iviews.ProjectorList.as_view()),
    url(r'^api/computers/add', iviews.ComputerList.as_view()),
    url(r'^api/systems/add', iviews.SystemList.as_view()),
    url(r'^api/email/add', iviews.EmailList.as_view()),
    url(r'^api/dcasset/add', iviews.DCAssetList.as_view()),
    url(r'^api/server/add', iviews.ServerList.as_view()),
    url(r'^api/software/add', iviews.SoftwareList.as_view()),
    url(r'^ownership/', include('Ownership.urls')),
    url(r'^api/computer/autocomplete', iviews.ComputerAutoComplete.as_view()),
    url(r'^api/system/autocomplete', iviews.SystemAutoComplete.as_view()),
    url(r'^api/email/autocomplete', iviews.EmailListAutoComplete.as_view()),
    url(r'^api/server/autocomplete', iviews.ServerAutoComplete.as_view()),
    url(r'^api/update/inventory/staff', oviews.UpdateStaffInventory.as_view()),
    url(r'^api/update/inventory/tenantlocation$', oviews.UpdateTenantLocationInventory.as_view()),
    url(r'^api/delete/inventory/tenantlocation$', oviews.DeleteTenantLocationInventory.as_view()),
    url(r'^api/update/inventory/customerlocation$', oviews.UpdateCustomerLocationInventory.as_view()),
    url(r'^api/delete/inventory/customerlocation$', oviews.DeleteCustomerLocationInventory.as_view()),
    url(r'^api/update/inventory/tenantlocation/server$', oviews.UpdateTenantServer.as_view()),
    url(r'^api/delete/inventory/tenantlocation/server$', oviews.DeleteTenantServer.as_view()),
    url(r'^api/update/inventory/customerlocation/server$', oviews.UpdateCustomerServer.as_view()),
    url(r'^api/delete/inventory/customerlocation/server$', oviews.DeleteCustomerServer.as_view()),
    url(r'^api/update/inventory/tenantlocation/projector$', oviews.UpdateTenantProjector.as_view()),
    url(r'^api/delete/inventory/tenantlocation/projector$', oviews.DeleteTenantProjector.as_view()),
    url(r'^api/update/inventory/customerlocation/projector$', oviews.UpdateCustomerProjector.as_view()),
    url(r'^api/delete/inventory/customerlocation/projector$', oviews.DeleteCustomerProjector.as_view()),
    url(r'^api/update/inventory/tenantlocation/datacenter$', oviews.UpdateTenantDataCenter.as_view()),
    url(r'^api/delete/inventory/tenantlocation/datacenter$', oviews.DeleteTenantDataCenter.as_view()),
    url(r'^api/update/inventory/customerlocation/datacenter$', oviews.UpdateCustomerDataCenter.as_view()),
    url(r'^api/delete/inventory/customerlocation/datacenter$', oviews.DeleteCustomerDataCenter.as_view()),
    url(r'^api/update/inventory/tenantlocation/system$', oviews.AddSystemForTenant.as_view()),
    url(r'^api/update/inventory/tenantlocation/software$', oviews.AddSoftwareForTenant.as_view()),
    url(r'^api/update/inventory/tenantlocation/software/developer$', oviews.UpdateSoftwareTenant.as_view()),
    url(r'^api/update/inventory/tenantlocation/system/developer$', oviews.UpdateSystemTenant.as_view()),
    url(r'^api/delete/inventory/tenantlocation/system/$', oviews.DeleteTenantSystem.as_view()),
    url(r'^api/delete/inventory/tenantlocation/software/$', oviews.DeleteTenantSoftware.as_view()),
    url(r'^api/update/inventory/customerlocation/system$', oviews.AddSystemForCustomer.as_view()),
    url(r'^api/update/inventory/customerlocation/software$', oviews.AddSoftwareForCustomer.as_view()),
    url(r'^api/update/inventory/customerlocation/software/developer$', oviews.UpdateSoftwareCustomer.as_view()),
    url(r'^api/update/inventory/customerlocation/system/developer$', oviews.UpdateSystemCustomer.as_view()),
    url(r'^api/delete/inventory/customerlocation/system/$', oviews.DeleteCustomerSystem.as_view()),
    url(r'^api/delete/inventory/customerlocation/software/$', oviews.DeleteCustomerSoftware.as_view()),
    url(r'^api/update/inventory/customer', oviews.UpdateProjectInventory.as_view()),
    url(r'^api/delete/inventory/customer', oviews.DeleteProjectInventory.as_view()),
    url(r'^api/update/inventory/department', oviews.UpdateDepartmentInventory.as_view()),
    url(r'^api/delete/inventory/department', oviews.DeleteDepartmentInventory.as_view()),
    url(r'^api/monitor/autocomplete', iviews.MonitorAutoComplete.as_view()),
    url(r'^api/projector/autocomplete', iviews.ProjectorAutoComplete.as_view()),
    url(r'^api/update/inventory/computer', iviews.ComputerUpdate.as_view()),
    url(r'^api/update/inventory/server', iviews.ServerUpdate.as_view()),
    url(r'^api/update/inventory/projector', iviews.ProjectorUpdate.as_view()),
    url(r'^api/update/inventory/monitor', iviews.MonitorUpdate.as_view()),
    url(r'^api/update/inventory/dcasset', iviews.DCAssetUpdate.as_view()),
    url(r'^api/staff/autocomplete', oviews.StaffAutoComplete.as_view()),
    url(r'^api/customer/autocomplete', oviews.ProjectAutoComplete.as_view()),
    url(r'^api/tenant/autocomplete', oviews.TenantAutoComplete.as_view()),
    url(r'^api/software/autocomplete', iviews.SoftwareAutoComplete.as_view()),
    url(r'^api/update/ownership/computer', iviews.UpdateComputerOwnership.as_view()),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', iviews.logout_user, name='logout'),
    url(r'^login/user$', iviews.login_user, name='login_user'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
