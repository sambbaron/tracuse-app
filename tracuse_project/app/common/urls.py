from django.conf.urls import url

from . import api
from . import views

urlpatterns = [

    # App Home
    url(r'^$', views.app_index, name='app_home'),

    # New API
    url(r'^datum_groups/$', api.datum_groups_get),

    # Tester Page
    url(r'^tester/$', views.datums_get, name="tester_home"),
    url(r'^tester/datum/(?P<datum_pk>[0-9]*)/update/$', views.datums_update, name='datums_update'),
    url(r'^tester/datum/(?P<datum_pk>[0-9]*)/delete/$', views.datums_delete, name='datums_delete'),
    url(r'^tester/datum/create/$', views.datums_create, name='datums_create'),

]

