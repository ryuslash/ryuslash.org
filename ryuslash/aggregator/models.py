from django.db import models

class Post(models.Model):
    post_id = models.CharField(max_length=255, unique=True,
                               primary_key=True)
    title = models.CharField(max_length=500, blank=True)
    category = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    updated = models.DateTimeField()
    content = models.TextField()
    icon = models.CharField(max_length=255)

    class Meta:
        ordering = [ '-updated' ]
