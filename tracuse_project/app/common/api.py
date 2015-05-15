"""API Endpoints"""

from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^datum_groups/$', views.datum_groups_get),
    url(r'^datum_types/$', views.datum_types_get),
    url(r'^datum_objects/$', views.datum_objects_get),

]