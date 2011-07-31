from __future__ import absolute_import

import json
import datetime

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from profiles.models import Child
from sources import youtube
from timeline.utils import age
from utils.json import ObjectEncoder

class YouTubeEvent(object):
    
    def __init__(self, video):
        self.id = video.url
        self.start = datetime.date(year=video.published.year, month=video.published.month, day=video.published.day).isoformat()
        self.title = video.title
        self.caption = video.title
        self.icon = video.thumbnails[1].url
        self.url = video.url


def start(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('timeline.views.logged_in'))
    else:
        events = json.dumps([YouTubeEvent(video) for video in youtube.list_videos('vorushin')], cls=ObjectEncoder)
        return render(request, 'timeline/start.html', { 'events' : events, 'body_class' : 'home' });

def logged_in(request, username):
    children = Child.objects.filter(user__username__exact=username)
    if not children:
        return HttpResponseRedirect(reverse('timeline.views.no_children'))
        
    return HttpResponseRedirect(reverse('timeline.views.timeline', args=[username, children[0].slug]))

def timeline(request, username, child_slug):
    events = json.dumps([YouTubeEvent(video) for video in youtube.list_videos('vorushin')], cls=ObjectEncoder)
    children = [dict(name='Marta', slug='marta', age=age(datetime.datetime(2010, 9, 22))), 
                dict(name='Eva', slug='eva', age=age(datetime.datetime(2009, 4, 18)))]
    return render(request, "timeline/timeline.html", 
                  { 'events' : events, 'children' : children, 'username' : username, 'current_child_slug' : child_slug})

# def events(request):
#     return HttpResponse(json.dumps(youtube.list_videos(username), cls=ObjectEncoder))
