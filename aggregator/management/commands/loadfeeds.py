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
                    updated = datetime.datetime(
                        entry.updated_parsed.tm_year,
                        entry.updated_parsed.tm_mon,
                        entry.updated_parsed.tm_mday,
                        entry.updated_parsed.tm_hour,
                        entry.updated_parsed.tm_min,
                        entry.updated_parsed.tm_sec)

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