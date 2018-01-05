from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^staff/(?P<staff_id>[0-9]+)$', views.staff_detail),
    url(r'^tenant/$', views.tenant_view),
    url(r'^tenant/(?P<tenant_id>[0-9]+)$', views.tenant_detail),
    url(r'^project/$', views.project_view),
    url(r'^project/(?P<project_id>[0-9]+)$', views.project_detail),
    url(r'^department/$', views.department_view),
    url(r'^department/(?P<department_id>[0-9]+)$', views.department_detail),

]
