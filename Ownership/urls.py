from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='ownership_index'),
    url(r'^staff/(?P<staff_id>[0-9]+)$', views.staff_detail),
    url(r'^tenant/$', views.tenant_view),
    url(r'^tenant/(?P<tenant_id>[0-9]+)$', views.tenant_detail),
    url(r'^customer/$', views.project_view),
    url(r'^customer/(?P<project_id>[0-9]+)$', views.customer_detail),
    url(r'^department/$', views.department_view),
    url(r'^department/(?P<department_id>[0-9]+)$', views.department_detail),
    url(r'^tenant/location/leasing/(?P<location_id>[0-9]+)$', views.tenant_location_detail,
        name="tenant_location_detail"),
    url(r'^tenant/location/dcportal/(?P<location_id>[0-9]+)$', views.tenant_location_rental,
        name="tenant_location_detail_dc_rental"),
    url(r'^tenant/location/systemandapps/(?P<location_id>[0-9]+)$', views.tenant_system_and_apps,
        name="tenant_location_detail_system_and_apps"),
    url(r'^customer/location/leasing/(?P<location_id>[0-9]+)$', views.customer_location_detail,
        name="customer_location_detail"),
    url(r'^customer/location/dcportal/(?P<location_id>[0-9]+)$', views.customer_location_rental,
        name="customer_location_detail_dc_rental"),
    url(r'^customer/location/systemandapps/(?P<location_id>[0-9]+)$', views.customer_system_and_apps,
        name="customer_location_detail_system_and_apps"),


]
