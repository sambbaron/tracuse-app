"""API Endpoints"""

from django.conf.urls import url

from app.datum import views as DatumViews
from app.element_type import views as ElementViews
from app.filter import views as FilterViews
from app.viewuse import views as ViewuseViews
from app.association import views as AssociationViews

urlpatterns = [

    # API Endpoints
    url(r'^datum_group/$', DatumViews.DatumGroupAll.as_view(), name="datum-group-all"),
    url(r'^datum_type/$', DatumViews.DatumTypeAll.as_view(), name="datum-type-all"),
    url(r'^datum_object/(?P<pk>[0-9]+)/$', DatumViews.DatumObjectOne.as_view(), name="datum-object-one"),
    url(r'^datum_object/$', DatumViews.DatumObjectAll.as_view(), name="datum-object-all"),

    url(r'^element_type/$', ElementViews.ElementTypeAll.as_view(), name="element-type-all"),
    url(r'^element_operator/$', ElementViews.ElementOperatorAll.as_view(), name="element-operator-all"),
    url(r'^element_datum_type/$', ElementViews.ElementDatumTypeAll.as_view(), name="element-datum-type-all"),
    url(r'^element_datum_object/(?P<pk>[0-9]+)/$', ElementViews.ElementDatumObjectOne.as_view(), name="element-datum-object-one"),
    url(r'^element_datum_object/$', ElementViews.ElementDatumObjectAll.as_view(), name="element-datum-object-all"),
    url(r'^element_option/$', ElementViews.ElementOptionAll.as_view(), name="element-option-all"),
    url(r'^element_data_type/$', ElementViews.ElementDataTypeAll.as_view(), name="element-data-type-all"),

    url(r'^viewuse_object/(?P<pk>[0-9]+)/$', ViewuseViews.ViewuseObjectOne.as_view(), name="viewuse-object-one"),
    url(r'^viewuse_object/$', ViewuseViews.ViewuseObjectAll.as_view(), name="viewuse-object-all"),
    url(r'^viewuse_arrangement/$', ViewuseViews.ViewuseArrangementAll.as_view(), name="viewuse-arrangement-all"),
    url(r'^viewuse_datum/$', ViewuseViews.ViewuseDatumAll.as_view(), name="viewuse-datum-all"),

    url(r'^filter/json/$', FilterViews.RunFilter.filter_from_json, name="filter-from-json"),
    url(r'^filter/(?P<pk>[0-9]+)/$', FilterViews.RunFilter.filter_from_set, name="filter-from-set"),

    url(r'^association_direction/$', AssociationViews.AssociationDirectionAll.as_view(), name="association-direction-all"),

]
