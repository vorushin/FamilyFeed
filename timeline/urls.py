from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('timeline.views',
    url(r'^timeline', 'timeline'),
)
