import json

from django.shortcuts import render

from sources import youtube
from utils.json import ObjectEncoder

class YouTubeEvent(object):
    
    def __init__(self, video):
        self.start = video.published.isoformat()
        self.title = video.title
        self.icon = video.thumbnails[1].url


def timeline(request):
    username = 'vorushin'
    # events = json.dumps([YouTubeEvent(video).__dict__ for video in youtube.list_videos(username)])
    events = json.dumps([YouTubeEvent(video) for video in youtube.list_videos(username)], cls=ObjectEncoder)
    return render(request, "timeline/timeline.html", { 'events' : events })


# def events(request):
#     return HttpResponse(json.dumps(youtube.list_videos(username), cls=ObjectEncoder))
