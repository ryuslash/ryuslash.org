from django.contrib.syndication.views import Feed
from django.contrib.comments.models import Comment

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

    def item_pubdate(self, item):
        return item.updated

class LatestCommentsFeed(Feed):
    title = "ryuslash's latest comments"
    link = "/"
    description = "Comments on posts"

    def items(self):
        return Comment.objects.all()

    def item_title(self, item):
        return 'Comment for %s' % item.content_object.title

    def item_description(self, item):
        return item.comment

    def item_link(self, item):
        return "/post/%s/" % item.object_pk

    def item_pubdate(self, item):
        return item.submit_date
