from django.conf.urls import patterns, url
from monitor import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^prev/(?P<id>\d+)$', views.prev, name='prev'),
    url(r'^recive_gps/$', views.recive_gps, name='recive_gps'),
    url(r'^recive_file/$', views.recive_file, name='recive_file'),
    url(r'^demo/$', views.demo, name='demo'),
)
