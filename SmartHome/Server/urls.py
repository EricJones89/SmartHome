from django.conf.urls import patterns, url
from Server import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^serial_connection/$', views.serial_connection, name='serial_connection'),
    url(r'^add_serial_connection/$', views.add_serial_connection, name='add_serial_connection'),
)
