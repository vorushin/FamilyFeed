from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('profiles.views',
    url(r'^$', 'start'),
    url(r'^registration/$', 'registration'),
    url(r'^youtube_feed/$', 'youtube_feed'),
    url(r'^facebook/done/$', 'facebook_login_done'),
)
