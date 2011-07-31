from urllib2 import urlopen
import json

def post_text(item):
    return item.get('message', u'') + item.get('description', u'')

def list_posts(access_token, first_5=False):
    graph_url = 'https://graph.facebook.com/me/feed?access_token=%s' % \
        access_token
    items = []

    resp = json.loads(urlopen(graph_url).read())
    while resp['data']:
        for item in resp['data']:
            if item.get('message'):
                items.append(item)
        if first_5:
            break
        resp = json.loads(urlopen(resp['paging']['next']).read())

    return items
