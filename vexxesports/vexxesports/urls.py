from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    #home page
    url(r'^$', 'maincontent.views.home', name='home'),

    #section pages
    url(r'^streams/', 'maincontent.views.streams', name='streams'),
    url(r'^matches/', 'maincontent.views.matches', name='matches'),
    url(r'^guides/', 'maincontent.views.guides', name='guides'),
    url(r'^team/', 'maincontent.views.teams', name='teams'),

    #admin urls
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
)
