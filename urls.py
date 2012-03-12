from django.conf.urls.defaults import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import DetailView

from aggregator.models import Post

urlpatterns = patterns('',
    url(r'^((?P<page>\d+)/)?$', 'aggregator.views.posts'),
    url(r'^post/((?P<pk>\d+)/)?$', DetailView.as_view(model=Post)))

urlpatterns += staticfiles_urlpatterns()
