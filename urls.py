from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import DetailView
from django.contrib import admin

from aggregator.models import Post

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^((?P<page>\d+)/)?$', 'aggregator.views.posts'),
    url(r'^post/((?P<pk>\d+)/)?$', DetailView.as_view(model=Post)),
    url(r'^admin/', include(admin.site.urls)))

urlpatterns += staticfiles_urlpatterns()
