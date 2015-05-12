from django.conf.urls import include, url
from django.contrib import admin

from website import views

urlpatterns = [

    url(r'^$', views.datums_get, name='datums_get'),
    url(r'^datum/(?P<datum_pk>[0-9]*)/update/$', views.datums_post, name='datums_post'),
    url(r'^datum/(?P<datum_pk>[0-9]*)/delete/$', views.datums_delete, name='datums_delete'),
    url(r'^datum/add/$', views.datums_add, name='datums_add'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('app.common.urls')),
]
