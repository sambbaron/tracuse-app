import json

from django.http import JsonResponse, HttpResponse, Http404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import (ViewuseObject,
                     ViewuseArrangement,
                     ViewuseDatum)
from .serializers import (ViewuseObjectSerializer,
                          ViewuseArrangementSerializer,
                          ViewuseDatumSerializer)
from app.common.serializers import Serializer


class ViewuseObjectAll(View):
    """Return all viewuse_objects"""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = ViewuseObject.actives.filter(Q(user=request.user) | Q(user=None)).all()
        serialized_data = Serializer(data=queryset,
                                     serializer=ViewuseObjectSerializer.serial_for_ui,
                                     dict_with_pk=True
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response


class ViewuseArrangementAll(View):
    """Return all viewuse_arrangements"""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = ViewuseArrangement.actives.all()
        serialized_data = Serializer(data=queryset,
                                     serializer=ViewuseArrangementSerializer.serial_basic,
                                     dict_with_pk=True
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response


class ViewuseDatumAll(View):
    """Return all viewuse_datums"""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = ViewuseDatum.actives.all()
        serialized_data = Serializer(data=queryset,
                                     serializer=ViewuseDatumSerializer.serial_basic,
                                     dict_with_pk=True
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response
