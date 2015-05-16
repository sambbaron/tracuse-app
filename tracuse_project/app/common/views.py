from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from app.datum.models import (DatumGroup,
                              DatumType,
                              DatumObject)


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'datum_objects': reverse('datum-objects-list', request=request, format=format)
    })

@login_required
def app_index(request):
    return render(request, "app/base_app.html")

@login_required
def datum_groups_get(request):
    datum_groups_orm = DatumGroup.actives.values()
    datum_groups_dict = dict(datum_group=list(datum_groups_orm))
    response = JsonResponse(datum_groups_dict)
    return response

@login_required
def datum_types_get(request):
    datum_types_orm = DatumType.actives.values()
    datum_types_dict = dict(datum_type=list(datum_types_orm))
    response = JsonResponse(datum_types_dict)
    return response

@login_required
def datum_objects_get(request):
    datum_objects_orm = DatumObject.actives.filter(user=request.user).values()
    datum_objects_dict = dict(datum_object=list(datum_objects_orm))
    response = JsonResponse(datum_objects_dict)
    return response

