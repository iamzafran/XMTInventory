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
    url(r'^api/update/inventory/staff', oviews.UpdateStaffInventory.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
