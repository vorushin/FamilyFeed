from django.db import models
from jsonfield import JSONField


class FacebookPost(models.Model):
    access_token = models.CharField(max_length=100)
    data = JSONField()
    created_time = models.DateTimeField()
