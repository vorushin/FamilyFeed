from django.contrib.auth.models import User
from django.db import models

from utils import make_uri_title


class Child(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    birthdate = models.DateField()

    def save(self, *args, **kwargs):
        self.slug = make_uri_title(self.name)
        return super(Child, self).save(*args, **kwargs)

    @property
    def facebook_keywords(self):
        if self.facebook_sources.all():
            return self.facebook_sources.all()[0].keywords
        else:
            return self.name

    @property
    def youtube_source(self):
        return YoutubeSource.objects.get_or_create(child=self)[0]

    @property
    def twitter_source(self):
        return TwitterSource.objects.get_or_create(child=self)[0]


class TwitterSource(models.Model):
    child = models.OneToOneField(Child, related_name='+')
    usernames = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)


class YoutubeSource(models.Model):
    child = models.OneToOneField(Child, related_name='+')
    usernames = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)


class FacebookSource(models.Model):
    child = models.ForeignKey(Child, related_name='facebook_sources')
    uid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)
    keywords = models.TextField()

    @property
    def picture(self):
        return 'https://graph.facebook.com/%s/picture' % self.uid
