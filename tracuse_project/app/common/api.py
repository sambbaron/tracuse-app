"""API Endpoints"""

from django.conf.urls import url

from app.datum.views import DatumObjectAll, DatumObjectOne

urlpatterns = [

    #API Endpoints
    url(r'^datum_objects/$', DatumObjectAll.as_view(), name="datum-object-all"),
    url(r'^datum_object/(?P<pk>[0-9]+)/$', DatumObjectOne.as_view(), name="datum-object-one"),

]