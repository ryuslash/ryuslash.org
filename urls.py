from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^((?P<page>\d+)/)?$', 'aggregator.views.posts'),
    url(r'^admin/', include(admin.site.urls)))

urlpatterns += staticfiles_urlpatterns()
