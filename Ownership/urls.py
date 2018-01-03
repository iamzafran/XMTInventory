from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^staff/(?P<staff_id>[0-9]+)$', views.staff_detail),

]
