from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^all/$', 'scheduler.views.schedules'),
	url(r'^all/(?P<stat>\d+)/$', 'scheduler.views.schedules'),
	url(r'^all/(?P<stat>\d+)/(?P<dfrom>\w+)/(?P<dto>\w+)/$', 'scheduler.views.schedules'),
	url(r'^schedule/(?P<schedule_id>\d+)/$', 'scheduler.views.schedule'),
	url(r'^create/$','scheduler.views.create'),
	url(r'^cancel/(?P<schedule_id>\d+)/$', 'scheduler.views.cancel_schedule'),
	url(r'^finish/(?P<schedule_id>\d+)/$', 'scheduler.views.finish_schedule'),
)
