from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse

import json

from utils.fb import facebook_callback

from sources import youtube

class ObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        return dict((k, v) for k, v in obj.__dict__.items() if not k.startswith("_"))

def start(request):
    return render(request, 'profiles/start.html')


def registration(request):
    return render(request, 'profiles/registration.html')


def youtube_feed(request):
    username = request.GET['username']
    return HttpResponse(json.dumps(youtube.list_videos(username), cls=ObjectEncoder))


@facebook_callback
def facebook_login_done(request, access_token):
    return HttpResponse(access_token)


# def facebook_login_done(request):
#     code = request.GET['code']
#     return HttpResponse(code)
