from __future__ import absolute_import

import json
import datetime

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from profiles.models import Child
from sources import youtube, facebook
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
        self.classname = 'video-event'

class FacebookEvent(object):

    def __init__(self, post):
        self.start = post['created_time']
        self.title = post['message']


def start(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('timeline.views.logged_in', args=[request.user]))
    else:
        events = json.dumps([YouTubeEvent(video) for video in youtube.list_videos('vorushin')], cls=ObjectEncoder)
        return render(request, 'timeline/start.html', { 'events' : events, 'body_class' : 'home' });

def logged_in(request, username):
    children = Child.objects.filter(user__username__exact=username)
    if not children:
        return render(request, 'timeline/no_profiles.html')
        
    return HttpResponseRedirect(reverse('timeline.views.timeline', args=[username, children[0].slug]))

def timeline(request, username, child_slug):
    child = Child.objects.get(user__username__exact=username, slug__exact=child_slug)
    children = Child.objects.filter(user__username__exact=username)
    facebook_events = []
    for facebook_source in child.facebook_sources:
        # TODO keywords
        facebook_events.extend(facebook.list_posts(facebook_source.access_token, first_5=True))
        print "+++++ ", facebook_source.access_token
    
    print "***** ", facebook_events
    
    # TODO keywords
    events = []
    events.extend([FacebookEvent(post) for post in facebook_events])
    events.extend([YouTubeEvent(video) for video in youtube.list_videos('vorushin')])
    events_json = json.dumps(events, cls=ObjectEncoder)
    children_data = [dict(name=child.name, slug=child.slug, age=age(child.birthdate)) for child in children]
    return render(request, "timeline/timeline.html", 
                  { 'events' : events_json, 'children' : children_data, 'username' : username, 'current_child_slug' : child_slug})

# def events(request):
#     return HttpResponse(json.dumps(youtube.list_videos(username), cls=ObjectEncoder))
