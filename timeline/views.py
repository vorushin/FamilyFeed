# -*- coding: utf-8 -*-

from __future__ import absolute_import

import json

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from profiles.models import Child
from sources import youtube, facebook
from utils import comma_split
from utils.json import ObjectEncoder

EXPECTED_TITLE_LEN = 30
def shorten(text):
    trim_index = text.find(' ', EXPECTED_TITLE_LEN)
    if trim_index != -1:
        return text[0:trim_index] + "..."
    else:
        return text


class YouTubeEvent(object):
    def __init__(self, video):
        self.type = 'youtube'
        self.id = video.url
        self.start = video.published.isoformat()
        self.title = video.title
        self.caption = video.title
        self.icon = video.thumbnails[1].url
        self.videoUrl = video.url
        self.classname = 'video-label'
        self.iconClassName = 'video-event'
        # self.classname = 'picture-label'


class FacebookEvent(object):
    def __init__(self, post):
        self.type = 'facebook'
        self.start = facebook.time(post['created_time']).isoformat()
        self.message = post.get('message', '')
        self.description = post.get('description', '')
        self.text = self.message
        if self.description:
            self.text += ' "%s"' % self.description
        self.title = shorten(self.message or self.description)
        self.url = post.get('link')
        post_picture = post.get('picture')
        if post_picture and post_picture.find('safe_image.php') == -1:
            self.icon = post_picture
        self.classname = 'facebook-label'
        self.iconClassName = 'facebook-icon'


def start(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(
            reverse('timeline.views.logged_in', args=[request.user]))
    else:
        videos = [YouTubeEvent(v) for v in youtube.list_videos('vorushin')]
        events = json.dumps(videos, cls=ObjectEncoder)
        return render(request,
                      'timeline/start.html',
                      {'events': events, 'body_class': 'home'})

def logged_in(request, username):
    children = Child.objects.filter(user__username__exact=username)
    if not children:
        return render(request, 'timeline/no_profiles.html')
    return HttpResponseRedirect(
        reverse('timeline.views.timeline', args=[username, children[0].slug]))

def keywords_present(items, keywords, text_func):
    result = []
    if not keywords:
        return items
    result = []
    for item in items:
        text = text_func(item)
        for keyword in keywords:
            if text.find(keyword) != -1:
                result.append(item)
                break
    return result

def timeline(request, username, child_slug):
    child = get_object_or_404(Child, user__username=username, slug=child_slug)
    children = Child.objects.filter(user__username__exact=username)

    facebook_events = []
    for facebook_source in child.facebook_sources.all():
        posts = facebook.list_posts(facebook_source.access_token)
        events = keywords_present(
            posts,
            comma_split(facebook_source.keywords),
            facebook.post_text)
        facebook_events.extend(events)

    youtube_source = child.youtube_source
    youtube_events = []
    if youtube_source.usernames:
        for youtube_user in comma_split(youtube_source.usernames):
            youtube_events.extend(
                keywords_present(youtube.list_videos(youtube_user),
                                 comma_split(youtube_source.keywords),
                                 lambda video: video.title))

    events = [FacebookEvent(post) for post in facebook_events] + \
             [YouTubeEvent(video) for video in youtube_events]
    events_json = json.dumps(events, cls=ObjectEncoder)
    return render(request,
                  'timeline/timeline.html',
                  {'events': events_json,
                   'children': children,
                   'username': username,
                   'current_child_slug': child_slug})
