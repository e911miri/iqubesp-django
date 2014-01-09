from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$','students.views.home', name='students_home'),
    url(r'^login$','django.contrib.auth.views.login', {'template_name': 'auth/login.djhtml'}, name='students_login'),
    url(r'^logout$','students.views.logout_view', name='students_logout'),
    url(r'^register/$','students.views.register_view', name='register'),
    
)