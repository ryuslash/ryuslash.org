from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from aggregator.feeds import LatestPostsFeed

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^((?P<cat>[a-z_-]+)/)?((?P<page>\d+)/)?$', 'aggregator.views.posts'),
    url(r'^feed/posts/$', LatestPostsFeed()),
)

urlpatterns += staticfiles_urlpatterns()
