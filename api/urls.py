"""Instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/$', views.PostList.as_view(), name='posts'),
    url(r'^posts/(?P<pk>[0-9]+)/$',  views.PostDetail.as_view(), name='post_detail'),
    url(r'^posts/(?P<pk>[0-9]+)/likes$', views.PostLikes.as_view(), name="like"),
    # url(r'^users/$', views.UserList.as_view(), name='users')
    # url(r'^auth/',include('rest_framework.urls'))
    # url(r'^images/$', views.getImage, name='images')

]
