import feedparser
import datetime
import markdown

from django.core.management.base import BaseCommand

from aggregator.models import Feed, Post

class Command(BaseCommand):
    help = "Load data from saved feeds."

    def handle(self, *args, **kwargs):
        feeds = Feed.objects.all()

        for feed in feeds:
            parsed = feedparser.parse(feed.get_feed_url())

            if 'title' in parsed.feed:
                feed.title = parsed.feed.title

            for entry in parsed.entries:
                if not Post.objects.filter(post_id=entry.id).exists():
                    dt = entry.updated_parsed \
                         or entry.published_parsed

                    if dt:
                        updated = datetime.datetime(
                            dt.tm_year, dt.tm_mon, dt.tm_mday,
                            dt.tm_hour, dt.tm_min, dt.tm_sec)
                    else:
                        updated = datetime.datetime.now()

                    post = Post(post_id=entry.id,
                                title=entry.title,
                                remote_url=entry.link,
                                updated=updated,
                                feed=feed)

                    if 'content' in entry.keys():
                        content = entry.content[0]['value']
                    else:
                        content = entry.summary

                    if feed.with_markdown:
                        post.body = markdown.markdown(content)
                    else:
                        post.body = content

                    post.save()

            if feed.post_set.count() > 0:
                last_updated = feed.post_set.order_by('-updated')[0]\
                                            .updated
                feed.updated = last_updated

            feed.save()
