from django.contrib.auth.models import User
from django.db import models


class Child(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    birthdate = models.DateField()

    @property
    def facebook_sources(self):
        return FacebookSource.objects.filter(child=self)


class DataSource(models.Model):
    child = models.ForeignKey(Child)
    keywords = models.TextField()


class TwitterSource(DataSource):
    username = models.CharField(max_length=15)


class YoutubeSource(DataSource):
    username = models.CharField(max_length=100)


class FacebookSource(DataSource):
    uid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)

    @property
    def picture(self):
        return 'https://graph.facebook.com/%s/picture' % self.uid
