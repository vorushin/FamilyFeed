from datetime import datetime
import json
from urllib2 import urlopen, HTTPError

from django.db.models import Max

from sources.models import FacebookPost

def time(s):
    return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S+0000')

def post_text(item):
    return item.get('message', u'') + item.get('description', u'')

def list_posts(access_token):
    latest_created_time = FacebookPost.objects\
        .filter(access_token=access_token)\
        .aggregate(Max('created_time'))['created_time__max']
    for post in new_posts(access_token, latest_created_time):
        if not FacebookPost.objects.filter(
                access_token=access_token,
                created_time=time(post['created_time'])).exists():
            FacebookPost.objects.create(
                access_token=access_token,
                created_time=time(post['created_time']),
                data=post)
    return [p.data for p in FacebookPost.objects \
                                        .filter(access_token=access_token) \
                                        .order_by('-created_time')]


def new_posts(access_token, older_than=None):
    graph_url = 'https://graph.facebook.com/me/feed?access_token=%s' % \
        access_token
    graph_url += '&limit=1000'
    if older_than:
        graph_url += '&since=' + older_than.isoformat()

    resp = json.loads(urlopen(graph_url).read())
    while resp['data']:
        for item in resp['data']:
            if older_than:
                if time(item['created_time']) <= older_than:
                    return
            if item.get('message'):
                yield item
        try:
            resp = json.loads(urlopen(resp['paging']['next']).read())
        except HTTPError:
            break
