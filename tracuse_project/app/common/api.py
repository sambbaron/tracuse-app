"""API Endpoints"""

from django.conf.urls import url

from app.datum import views as DatumViews
from app.element_type import views as ElementViews
from app.filter import views as FilterViews
from app.viewuse import views as ViewuseViews

urlpatterns = [

    # API Endpoints
    url(r'^datum_groups/$', DatumViews.DatumGroupAll.as_view(), name="datum-group-all"),
    url(r'^datum_types/$', DatumViews.DatumTypeAll.as_view(), name="datum-type-all"),
    url(r'^datum_objects/$', DatumViews.DatumObjectAll.as_view(), name="datum-object-all"),
    url(r'^datum_object/(?P<pk>[0-9]+)/$', DatumViews.DatumObjectOne.as_view(), name="datum-object-one"),

    url(r'^element_types/$', ElementViews.ElementTypeAll.as_view(), name="element-type-all"),
    url(r'^element_operators/$', ElementViews.ElementOperatorAll.as_view(), name="element-operator-all"),
    url(r'^element_datum_types/$', ElementViews.ElementDatumTypeAll.as_view(), name="element-datum-type-all"),
    url(r'^element_datum_objects/$', ElementViews.ElementDatumObjectAll.as_view(), name="element-datum-object-all"),
    url(r'^element_datum_object/(?P<pk>[0-9]+)/$', ElementViews.ElementDatumObjectOne.as_view(), name="element-datum-object-one"),

    url(r'^viewuse_objects/$', ViewuseViews.ViewuseObjectAll.as_view(), name="viewuse-object-all"),
    url(r'^viewuse_arrangements/$', ViewuseViews.ViewuseArrangementAll.as_view(), name="viewuse-arrangement-all"),
    url(r'^viewuse_datums/$', ViewuseViews.ViewuseDatumAll.as_view(), name="viewuse-datum-all"),

    url(r'^filter/json/$', FilterViews.RunFilter.filter_from_json, name="filter-from-json"),
    url(r'^filter/(?P<pk>[0-9]+)/$', FilterViews.RunFilter.filter_from_set, name="filter-from-set"),


]
