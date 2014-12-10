from django.conf.urls import patterns, url
from xbee_module import views

urlpatterns = patterns('',
    url(r'^program/(?P<xbee_module_id>[0-9]+)/$', views.program, name='program'),
    # url(r'^program/$', views.program, name='program'),
)