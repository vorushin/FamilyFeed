from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('timeline.views',
    url(r'^$', 'start'),
    url(r'^timeline', 'timeline'),
)
