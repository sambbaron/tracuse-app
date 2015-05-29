"""API Endpoints"""

from django.conf.urls import url

from app.datum import views as DatumViews
from app.element_type import views as ElementViews
from app.filter import views as FilterViews

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

    url(r'^datum_objects/filter/manual/$', FilterViews.RunFilter.run_filter_manual, name="datum-objects-filter-manual"),
    # url(r'^datum_objects/filter/(?P<pk>[0-9]+)/$', FilterViews, name="datum-objects-filter-saved-set"),

]
