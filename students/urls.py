from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$','students.views.home', name='students_home'),
)