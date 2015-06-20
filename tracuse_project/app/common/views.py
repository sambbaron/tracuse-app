from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.test import RequestFactory

from app.datum.views import DatumGroupAll, DatumTypeAll
from app.element_type.views import ElementTypeAll, ElementDatumTypeAll, ElementOperatorAll
from app.viewuse.views import ViewuseObjectAll, ViewuseArrangementAll, ViewuseDatumAll


@login_required
def app_index(request):
    """Load app with bootstrapped data
    """
    bootstrap_views = [DatumGroupAll, DatumTypeAll,
                       ElementTypeAll, ElementDatumTypeAll, ElementOperatorAll,
                       ViewuseObjectAll, ViewuseArrangementAll, ViewuseDatumAll
                       ]

    bootstrap_request = RequestFactory().get("")
    bootstrap_request.user = request.user

    bootstrap_data = {}
    for view_class in bootstrap_views:
        view_key = view_class.model.__name__
        view_object = view_class(request=bootstrap_request)
        view_data = view_object.dispatch(request=bootstrap_request).content.decode()
        bootstrap_data[view_key] = view_data

    return render(request, "app/base_app.html", {"bootstrap_data": bootstrap_data})
