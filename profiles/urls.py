from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('profiles.views',
    url(r'^$', 'start'),
    url(r'^registration/$', 'registration'),
    url(r'^add_child/$', 'add_child'),
    url(r'^feeds/youtube$', 'youtube_feed'),
    url(r'^feeds/facebook$', 'facebook_feed'),
    url(r'^facebook/done/$', 'facebook_login_done'),
)
