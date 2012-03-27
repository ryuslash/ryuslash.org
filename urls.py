from django.conf.urls.defaults import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import DetailView

from aggregator.models import Post
from aggregator.feeds import LatestPostsFeed, LatestCommentsFeed

urlpatterns = patterns('',
    url(r'^post/(?P<pk>\d+)/$', DetailView.as_view(model=Post)),
    url(r'^((?P<cat>[a-z_-]+)/)?((?P<page>\d+)/)?$',
        'aggregator.views.posts'),
    url(r'^feed/posts/$', LatestPostsFeed()),
    url(r'^feed/comments/$', LatestCommentsFeed()),
    url(r'^comments/', include('django.contrib.comments.urls')))

urlpatterns += staticfiles_urlpatterns()
