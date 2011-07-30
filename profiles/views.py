import json

from django.contrib.auth import authenticate, login as auth_login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

import json

from profiles.forms import RegistrationForm
from sources import youtube, facebook

from utils.json import ObjectEncoder

from utils.fb import facebook_callback


def start(request):
    return render(request, 'profiles/start.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                                password=form.cleaned_data['password'])
            auth_login(request, user)
            return HttpResponseRedirect(reverse('profiles.views.add_child'))
    else:
        form = RegistrationForm()
    return render(request, 'profiles/registration.html', {'form': form})


def add_child(request):
    return HttpResponse('add child')


def youtube_feed(request):
    username = request.GET['username']
    return HttpResponse(json.dumps(youtube.list_videos(username), cls=ObjectEncoder))

def facebook_feed(request):
    token = 'TODO'
    username = request.GET['username']
    return HttpResponse(json.dumps(facebook.list_posts(username, token)))


@facebook_callback
def facebook_login_done(request, access_token):
    return HttpResponse(access_token)
