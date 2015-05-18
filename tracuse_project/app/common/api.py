"""API Endpoints"""

from django.conf.urls import url

from app.datum import views as DatumViews

urlpatterns = [

    #API Endpoints
    url(r'^datum_groups/$', DatumViews.DatumGroupAll.as_view(), name="datum-group-all"),
    url(r'^datum_types/$', DatumViews.DatumTypeAll.as_view(), name="datum-type-all"),
    url(r'^datum_objects/$', DatumViews.DatumObjectAll.as_view(), name="datum-object-all"),
    url(r'^datum_object/(?P<pk>[0-9]+)/$', DatumViews.DatumObjectOne.as_view(), name="datum-object-one"),

]