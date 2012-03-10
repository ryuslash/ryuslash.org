from django.db import models

class Feed(models.Model):
    name = models.CharField(max_length=200)
    base_url = models.URLField(max_length=255)
    feed_url = models.CharField(max_length=255)
    profile_url = models.CharField(max_length=255)
    favicon_ext = models.CharField(max_length=4)
    title = models.CharField(max_length=500, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    uses_title = models.BooleanField(default=False)
    br2nl = models.BooleanField(default=False)

    def get_profile_url(self):
        return self.base_url + self.profile_url

    def get_feed_url(self):
        return self.base_url + self.feed_url

    def get_favicon_url(self):
        return self.base_url + 'favicon.' + self.favicon_ext

class Post(models.Model):
    post_id = models.CharField(max_length=500, unique=True)
    title = models.CharField(max_length=500)
    body = models.TextField()
    remote_url = models.URLField(max_length=255)
    updated = models.DateTimeField()
    added = models.DateTimeField(auto_now_add=True)
    feed = models.ForeignKey(Feed)
