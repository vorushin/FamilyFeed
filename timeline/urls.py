from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('timeline.views',
    url(r'^$', 'start'),
    url(r'^(?P<username>[\w.@+-]+)/$', 'logged_in'),
    url(r'^(?P<username>[\w.@+-]+)/(?P<child_slug>[\w.@+-]+)$',
        'timeline'),
)
