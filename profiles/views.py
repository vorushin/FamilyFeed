import json

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render

from profiles.forms import ChildForm, RegistrationForm
from profiles.models import Child
from sources import youtube, facebook

from utils import make_uri_title
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


@login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST, user=request.user)
        if form.is_valid():
            child = form.save()
            url = reverse(
                'profiles.views.edit_child',
                args=[request.user.username, make_uri_title(child.name)])
            return HttpResponseRedirect(url)
    else:
        form = ChildForm()
    return render(request,
                  'profiles/add_child.html',
                  {'is_add': True,
                   'form': form})


@login_required
def edit_child(request, username, child_name):
    user = get_object_or_404(User, username=username)
    child = get_object_or_404(Child, user=user, name=child_name)
    return render(request, 'profiles/edit_child.html', {'child': child})


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
