from django.shortcuts import render

import json


def start(request):
    return render(request, 'profiles/start.html')


def registration(request):
    return render(request, 'profiles/registration.html')


def youtube_feed(request):
    username = request.POST['username']
    return json.dumps([video for video in youtube.list_videos(username)])
