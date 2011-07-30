from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('profiles.views',
    url(r'^$', 'start'),
    url(r'^registration/$', 'registration'),
    url(r'^add_child/$', 'add_child'),
    url(r'^youtube_feed/$', 'youtube_feed'),
)
