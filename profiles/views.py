import json

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from profiles.forms import ChildForm, RegistrationForm
from sources import youtube, facebook
from utils import make_uri_title
from utils.fb import facebook_callback

from utils.json import ObjectEncoder
from utils.fb import facebook_callback


class ObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        return dict((k, v) for k, v in obj.__dict__.items()
                           if not k.startswith("_"))


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


@login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST, user=request.user)
        if form.is_valid():
            child = form.save()
            url = reverse('profiles.views.edit_child',
                          args=[make_uri_title(child.name)])
            return HttpResponseRedirect(url)
    else:
        form = ChildForm()
    return render(request,
                  'profiles/add_child.html',
                  {'is_add': True,
                   'form': form})


def youtube_feed(request):
    username = request.GET['username']
    return HttpResponse(json.dumps(youtube.list_videos(username),
                                   cls=ObjectEncoder))


def facebook_feed(request):
    token = 'TODO'
    username = request.GET['username']
    return HttpResponse(json.dumps(facebook.list_posts(username, token)))


@facebook_callback
def facebook_login_done(request, access_token):
    return HttpResponse(access_token)
