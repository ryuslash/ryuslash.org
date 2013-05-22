import datetime
import feedparser
import markdown
import os
import re
import urllib2

from django.conf import settings
from django.core.management.base import BaseCommand

from aggregator.models import Feed, Post


class Command(BaseCommand):
    help = "Load data from saved feeds."

    def prep_feedname(self, value):
        value = re.sub('[^\w\s-]', '', value).strip().lower()
        return re.sub('[-\s]+', '-', value)

    def get_logopath(self, feed):
        ext = feed.favicon_ext
        filename = self.prep_feedname(feed.name) + '.' + ext
        basedir = settings.STATICFILES_DIRS[0]
        return os.path.join(basedir, 'images/logos', filename)

    def have_logo(self, feed):
        logopath = self.get_logopath(feed)
        return os.path.exists(logopath)

    def save_logo(self, feed):
        ext = feed.favicon_ext
        url = feed.base_url + '/favicon.' + ext

        try:
            logo = urllib2.urlopen(url)
        except:
            return

        save = open(self.get_logopath(feed), 'w')

        save.write(logo.read())
        save.close()
        logo.close()

    def construct_feed_url(self, feed):
        return feed.base_url + feed.feed_url

    def handle(self, *args, **kwargs):
        for feed in Feed.objects.all():
            parsed = feedparser.parse(self.construct_feed_url(feed))
            icon = self.prep_feedname(feed.name) + '.' + feed.favicon_ext
            newcount = 0

            if not self.have_logo(feed):
                self.save_logo(feed)

            for entry in parsed.entries:
                if Post.objects.filter(post_id=entry.id).exists():
                    continue

                dt = entry.updated_parsed or entry.published_parsed

                if dt:
                    updated = datetime.datetime(
                        dt.tm_year, dt.tm_mon, dt.tm_mday,
                        dt.tm_hour, dt.tm_min, dt.tm_sec)
                else:
                    updated = datetime.datetime.now()

                if 'content' in entry.keys():
                    content = entry.content[0]['value']
                else:
                    content = entry.summary

                if feed.uses_markdown:
                    content = markdown.markdown(content)

                if feed.convert_newlines:
                    content = re.sub('\n', '</br>\n', content)

                post = Post(
                    post_id=entry.id,
                    title=entry.title if feed.uses_titles else '',
                    link=entry.link,
                    updated=updated,
                    icon=icon,
                    content=content,
                    feed=feed
                )

                post.save()
                newcount += 1

            print 'Grabbed %d new posts from %s' % (newcount, feed.name)
