import json
import datetime

from django.shortcuts import render

from sources import youtube
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
        return HttpResponseRedirect(reverse('timeline'))
    else:
        return render(request, 'timeline/start.html')

def timeline(request):
    username = 'vorushin'
    # events = json.dumps([YouTubeEvent(video).__dict__ for video in youtube.list_videos(username)])
    events = json.dumps([YouTubeEvent(video) for video in youtube.list_videos(username)], cls=ObjectEncoder)
    return render(request, "timeline/timeline.html", { 'events' : events })


# def events(request):
#     return HttpResponse(json.dumps(youtube.list_videos(username), cls=ObjectEncoder))
