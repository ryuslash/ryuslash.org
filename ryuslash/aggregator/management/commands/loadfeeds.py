import feedparser
import datetime
import markdown
import re
import os
import urllib2

from django.core.management.base import BaseCommand

from aggregator.models import Post
import settings

class Command(BaseCommand):
    help = "Load data from saved feeds."

    def prep_feedname(self, value):
        value = re.sub('[^\w\s-]', '', value).strip().lower()
        return re.sub('[-\s]+', '-', value)

    def get_ext(self, options):
        if 'favicon_ext' in options.keys():
            return options['favicon_ext']
        else:
            return 'ico'

    def get_logopath(self, feedname, options):
        ext = self.get_ext(options)
        filename = self.prep_feedname(feedname) + '.' + ext
        basedir = os.path.dirname(os.path.abspath(settings.__file__))
        return os.path.join(basedir, 'static/images/logos', filename)

    def have_logo(self, feedname, options):
        logopath = self.get_logopath(feedname, options)
        return os.path.exists(logopath)

    def save_logo(self, feedname, options):
        ext = self.get_ext(options)
        url = options['base_url'] + '/favicon.' + ext

        try:
            logo = urllib2.urlopen(url)
        except:
            return

        save = open(self.get_logopath(feedname, options), 'w')

        save.write(logo.read())
        save.close()
        logo.close()

    def construct_feed_url(self, feed):
        return feed['base_url'] + feed['feed_url']

    def handle(self, *args, **kwargs):
        for feedname, feedoptions in settings.FEEDS.iteritems():
            parsed = \
                feedparser.parse(self.construct_feed_url(feedoptions))
            icon = self.prep_feedname(feedname) + '.' \
                   + self.get_ext(feedoptions)
            newcount = 0

            if not self.have_logo(feedname, feedoptions):
                self.save_logo(feedname, feedoptions)

            for entry in parsed.entries:
                if Post.objects.filter(post_id=entry.id).exists():
                    continue

                dt = entry.updated_parsed \
                     or entry.published_parsed

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

                if feedoptions['markdown']:
                    content = markdown.markdown(content)

                if feedoptions.get('nl2br'):
                    content = re.sub('\n', '</br>\n', content)

                post = Post(post_id=entry.id,
                            title=entry.title,
                            category=feedoptions['category'],
                            link=entry.link,
                            updated=updated,
                            icon=icon,
                            content=content)

                post.save()
                newcount += 1

            print 'Grabbed %d new feeds from %s' % (newcount, feedname)
