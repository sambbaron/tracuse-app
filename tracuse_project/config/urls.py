from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from website import views
from app.common import views_tester

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name="website/base_website.html"), name='index'),
    url(r'^more/$', TemplateView.as_view(template_name="website/more.html"), name='more'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('app.common.urls')),
    url(r'^api/', include('app.common.api')),


    # Tester Page
    url(r'^tester/$', views_tester.datums_get, name="tester_home"),
    url(r'^tester/datum/(?P<datum_pk>[0-9]*)/update/$', views_tester.datums_update, name='datums_update'),
    url(r'^tester/datum/(?P<datum_pk>[0-9]*)/delete/$', views_tester.datums_delete, name='datums_delete'),
    url(r'^tester/datum/create/$', views_tester.datums_create, name='datums_create'),

]
