from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'honey.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^monitor/', include('monitor.urls', namespace='monitor')),
)
