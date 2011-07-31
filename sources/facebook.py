from urllib2 import urlopen
import json

def keywords_present(item, keywords):
    if not keywords:
        return True
    text = item.get('message', u'') + item.get('description', u'')
    for keyword in keywords:
        if text.find(keyword) != -1:
            return False
    return True
    
def list_posts(access_token, keywords=[], first_5=False):
    graph_url = 'https://graph.facebook.com/me/feed?access_token=%s' % \
        access_token
    items = []

    resp = json.loads(urlopen(graph_url).read())
    while resp['data']:
        for item in resp['data']:
            if item.get('message') and keywords_present(item, keywords):
                items.append(item)
        if first_5:
            break
        resp = json.loads(urlopen(resp['paging']['next']).read())

    return items
