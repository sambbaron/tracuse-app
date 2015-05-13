from django.conf.urls import include, url
from django.contrib import admin

from website import views

urlpatterns = [

    url(r'^$', views.datums_get, name='datums_get'),
    url(r'^datum/(?P<datum_pk>[0-9]*)/update/$', views.datums_update, name='datums_update'),
    url(r'^datum/(?P<datum_pk>[0-9]*)/delete/$', views.datums_delete, name='datums_delete'),
    url(r'^datum/create/$', views.datums_create, name='datums_create'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('app.common.urls')),
]
