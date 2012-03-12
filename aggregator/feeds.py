from django.contrib.syndication.views import Feed

from .models import Post

class LatestPostsFeed(Feed):
    title = "ryuslash's RSS feed"
    link = "/"
    description = "Updates by ryuslash"

    def items(self):
        return Post.objects.all()[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return "/post/%d/" % item.pk
