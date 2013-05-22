from django.db import models

CATEGORIES = ['post', 'activity']


class Feed(models.Model):
    name = models.CharField(max_length=300)
    base_url = models.URLField()
    feed_url = models.CharField(max_length=100)
    favicon_ext = models.CharField(max_length=10, default='ico')
    uses_markdown = models.BooleanField()
    uses_titles = models.BooleanField()
    convert_newlines = models.BooleanField()
    category = models.SmallIntegerField(
        choices=[(CATEGORIES.index(c), c) for c in CATEGORIES]
    )

    def __unicode__(self):
        return self.name


class Post(models.Model):
    post_id = models.CharField(max_length=255, unique=True,
                               primary_key=True)
    title = models.CharField(max_length=500, blank=True)
    link = models.URLField(max_length=255)
    updated = models.DateTimeField()
    content = models.TextField()
    icon = models.CharField(max_length=255)
    feed = models.ForeignKey(Feed)

    class Meta:
        ordering = ['-updated']
