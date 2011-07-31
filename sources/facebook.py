import urllib2
import json


def list_posts(username, access_token, keywords=[]):
    graph_url = 'https://graph.facebook.com/me/feed?access_token=%s' % \
        access_token
    keywords = split_keywords(keywords)
    items = []

    resp = json.loads(urlopen(graph_url).read())
    while resp['data']:
        for item in resp['data']:
            text = item.get('message', u'') + item.get('description', u'')
            for keyword in keywords:
                if text.find(keyword) != -1:
                    items.append(item)
                    break
        resp = json.loads(urlopen(resp['paging']['next']).read())

    return items
