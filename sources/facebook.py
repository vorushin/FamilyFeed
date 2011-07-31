import urllib2
import json


def list_posts(username, access_token):
    return json.loads(_fetch_posts(username, access_token))


def _fetch_posts(username, access_token):
    url = 'https://graph.facebook.com/%s/posts?access_token=%s' % \
        (username, access_token)
    response = urllib2.urlopen(url)
    return response.read()
