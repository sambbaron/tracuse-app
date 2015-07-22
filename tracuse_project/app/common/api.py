"""API Endpoints"""

from django.conf.urls import url

from app.datum import views as DatumViews
from app.element_type import views as ElementViews
from app.filter import views as FilterViews
from app.ui_object import views as UiObjectViews
from app.viewuse import views as ViewuseViews
from app.windowuse import views as WindowuseViews
from app.association import views as AssociationViews
from app.tracuser import views as TracuserViews

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
    
    url(r'^ui_arrangement_type/$', UiObjectViews.UiArrangementTypeAll.as_view(), name="ui-arrangement-type-all"),
    url(r'^ui_formatting_type/$', UiObjectViews.UiFormattingTypeAll.as_view(), name="ui-formatting-type-all"),

    url(r'^viewuse_object/(?P<pk>[0-9]+)/$', ViewuseViews.ViewuseObjectOne.as_view(), name="viewuse-object-one"),
    url(r'^viewuse_object/$', ViewuseViews.ViewuseObjectAll.as_view(), name="viewuse-object-all"),

    url(r'^windowuse_object/(?P<pk>[0-9]+)/$', WindowuseViews.WindowuseObjectOne.as_view(), name="windowuse-object-one"),
    url(r'^windowuse_object/$', WindowuseViews.WindowuseObjectAll.as_view(), name="windowuse-object-all"),
    url(r'^windowuse_viewuse/(?P<pk>[0-9]+)/$', WindowuseViews.WindowuseViewuseOne.as_view(), name="windowuse-viewuse-one"),
    url(r'^windowuse_viewuse/$', WindowuseViews.WindowuseViewuseAll.as_view(), name="windowuse-viewuse-all"),

    url(r'^filter/json/$', FilterViews.RunFilter.filter_from_json, name="filter-from-json"),
    url(r'^filter/(?P<pk>[0-9]+)/$', FilterViews.RunFilter.filter_from_set, name="filter-from-set"),

    url(r'^association_direction/$', AssociationViews.AssociationDirectionAll.as_view(), name="association-direction-all"),

    url(r'^tracuser_landing/$', TracuserViews.TracuserLandingAll.as_view(), name="tracuser-landing-all"),

]
