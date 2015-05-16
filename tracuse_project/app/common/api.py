"""API Endpoints"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views as CommonViews
from app.datum import views as DatumViews

urlpatterns = [

    #API Endpoints
    url(r'^$', CommonViews.api_root),
    url(r'^datum_objects/$', DatumViews.DatumObjectList.as_view(), name="datum-objects-list"),
    url(r'^datum_object/(?P<pk>[0-9]+)/$', DatumViews.DatumObjectDetail.as_view(), name="datum-objects-detail"),

    #url(r'^datum_groups/$', views.datum_groups_get),
    #url(r'^datum_types/$', views.datum_types_get),
    #url(r'^datum_objects/$', views.datum_objects_get),

]

urlpatterns = format_suffix_patterns(urlpatterns)