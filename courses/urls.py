from django.conf.urls import patterns, url
import courses.views

urlpatterns = patterns('',
    url(r'^$',courses.views.index.as_view(), name='courses_index'),
#     url(r'^(?P<course_id>\d+)$',courses.views.details, name='course_detail'),
#     url(r'^(?P<course_id>\d+)/register$', courses.views.register, name='course_register'),
    
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)$',courses.views.details, name='course_detail'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/register$', courses.views.register, name='course_register'),
)