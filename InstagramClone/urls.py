from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
from stream import views
from django.conf import settings
from django.conf.urls.static import static
from management import views as management_views
=======
>>>>>>> f6b0725a8259763ac3f0e775153b6c3a484d631b

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'InstagramClone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
<<<<<<< HEAD
    url(r'^$', views.home, name='home'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^accounts/register/$', management_views.register, name='register'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
)
>>>>>>> f6b0725a8259763ac3f0e775153b6c3a484d631b
