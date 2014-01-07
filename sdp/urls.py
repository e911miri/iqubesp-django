from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    url(r'^accounts/profile/$', 'home.views.index', name='profile'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.djhtml'}),
    
    url(r'^courses/', include('courses.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)