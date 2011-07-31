from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('profiles.views',
    url(r'^$', 'start'),
    url(r'^registration/$', 'registration'),

    url(r'^add_child/$', 'add_child'),
    url(r'^(?P<username>[\w.@+-]+)/(?P<child_slug>[\w.@+-]+)/edit$',
         'edit_child'),
    url(r'^feeds/youtube$', 'youtube_feed'),
    url(r'^feeds/facebook$', 'facebook_feed'),
    url(r'^facebook/done/$', 'facebook_login_done'),

    url(r'^(?P<username>[\w.@+-]+)/(?P<child_slug>[\w.@+-]+)/add_fb/$',
        'add_facebook_profile'),
    url(r'^(?P<username>[\w.@+-]+)/(?P<child_slug>[\w.@+-]+)/add_fb_done/$',
        'add_facebook_profile_done'),

    url(r'^(?P<username>[\w.@+-]+)/(?P<child_slug>[\w.@+-]+)/fb_data_ajax/$',
        'get_facebook_data_ajax'),
)

urlpatterns += patterns('',
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'profiles/login.html'},
        name='login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name='logout'),
)
