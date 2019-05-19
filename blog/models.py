from django.conf import settings
from django.db import models
from django.utils import timezone

class Images(models.Model):
    IMAGES_TYPES = (
        ('D', 'Drawings'),
        ('P', 'Pictures'),
    )
    title = models.CharField(max_length=80)
    type = models.CharField(max_length=1, choices=IMAGES_TYPES)
    png_image = models.CharField(max_length=1000)

class Post(models.Model):
    ARTICLE_TYPE = (
        ('T', 'Travel'),
        ('S', 'Sport'),
        ('D', 'Design'),

    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=1, choices=ARTICLE_TYPE)
    image =models.ForeignKey(Images, on_delete=models.DO_NOTHING)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
