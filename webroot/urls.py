from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from codecamp.models import Speaker, Session

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codecamp.views.home', name='home'),
    # url(r'^codecamp/', include('codecamp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^speakers$', redirect_to, {'url': '/speakers/'}),
    url(r'^speakers/$', 'codecamp.views.speakers_index', name='speaker_index'),
    url(r'^speakers/(?P<slug>[-\w\d]+),(?P<id>\d+)/$','codecamp.views.speaker_detail', name='speaker_detail'),
    (r'^sessions$', redirect_to, {'url': '/sessions/'}),
    url(r'^sessions/$', 'codecamp.views.sessions_index', name='session_index'),
    url(r'^sessions/(?P<slug>[-\w\d]+),(?P<id>\d+)/$','codecamp.views.session_detail', name='session_detail'),
    (r'', include('django.contrib.flatpages.urls')),
    
)
