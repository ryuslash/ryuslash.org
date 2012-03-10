import feedparser
import datetime

from django.core.management.base import BaseCommand

from aggregator.models import Feed, Post

class Command(BaseCommand):
    help = "hi"

    def handle(self, *args, **kwargs):
        feeds = Feed.objects.all()

        for feed in feeds:
            parsed = feedparser.parse(feed.get_feed_url())
            feed.title = parsed.feed.title

            for entry in parsed.entries:
                if not Post.objects.filter(post_id=entry.id).exists():
                    updated = datetime.datetime(
                        entry.updated_parsed.tm_year,
                        entry.updated_parsed.tm_mon,
                        entry.updated_parsed.tm_mday,
                        entry.updated_parsed.tm_hour,
                        entry.updated_parsed.tm_min,
                        entry.updated_parsed.tm_sec)

                    post = Post(post_id=entry.id,
                                title=entry.title,
                                body=entry.summary,
                                remote_url=entry.link,
                                updated=updated,
                                feed=feed)
                    post.save()

            last_updated = Post.objects.filter(feed=feed)\
                                       .order_by('-updated')[0].updated
            feed.updated = last_updated
            feed.save()
