from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from aggregator.feeds import LatestPostsFeed

admin.autodiscover()

urlpatterns = patterns(
    'aggregator.views',
    url(r'^$', 'posts', name='index'),
    url(r'^(?P<page>\d+)/$', 'posts', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<cat>[a-z_-]+)/$', 'posts', name='index'),
    url(r'^(?P<cat>[a-z_-]+)/(?P<page>\d+)/$', 'posts', name='index'),
    url(r'^feed/posts/$', LatestPostsFeed()),
)

urlpatterns += staticfiles_urlpatterns()
