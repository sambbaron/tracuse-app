from django.conf.urls import include, url
from django.contrib import admin

from website import views

urlpatterns = [

    url(r'^$', views.user_login, name='index'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('app.common.urls')),

]
