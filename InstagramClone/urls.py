from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from stream import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'InstagramClone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
