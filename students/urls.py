from django.conf.urls import patterns, url
import students.views

urlpatterns = patterns('',
    url(r'^$',students.views.home, name='students_home'),
    url(r'^login/(\w*)',students.views.login, name='students_login'),
)