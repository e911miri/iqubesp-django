from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    url(r'^accounts/profile/$', 'home.views.index', name='profile'),
    url(r'^login/(\w*)', 'home.views.login', name='login'),
    
    
    url(r'^courses/', include('courses.urls')),
    url(r'^students/', include('students.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)