from django.shortcuts import render


def start(request):
    return render(request, 'profiles/start.html')


def registration(request):
    return render(request, 'profiles/registration.html')


def youtube_feed(request):
    return ""
