from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/$', 'proj.views.login'),
	url(r'^accounts/auth/$', 'proj.views.auth_view'),
	url(r'^accounts/logout/$', 'proj.views.logout'),
	url(r'^accounts/loggedin/$', 'proj.views.loggedin'),
	url(r'^accounts/invalid/$', 'proj.views.invalid_login'),
	url(r'^accounts/register/$', 'proj.views.register_user'),
	url(r'^accounts/register_success/$', 'proj.views.register_success'),
	
	url(r'^scheduler/', include('scheduler.urls')),
)
