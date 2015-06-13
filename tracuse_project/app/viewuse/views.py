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
    model_name = "ViewuseObject"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = ViewuseObject.actives.filter(Q(user=request.user) | Q(user=None)).all()
        serialized_data = Serializer(data=queryset,
                                     serializer=ViewuseObjectSerializer.serial_basic
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200, safe=False)
        return response


class ViewuseObjectOne(View):
    model_name = "ViewuseObject"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return ViewuseObject.objects.get(pk=pk)
        except ViewuseObject.DoesNotExist:
            raise Http404("Viewuse Object does not exist.")

    def get(self, request, pk):
        object = self.get_object(pk)
        serialized_data = Serializer(data=object,
                                     serializer=ViewuseObjectSerializer.serial_basic
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response


class ViewuseArrangementAll(View):
    model_name = "ViewuseArrangement"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = ViewuseArrangement.actives.all()
        serialized_data = Serializer(data=queryset,
                                     serializer=ViewuseArrangementSerializer.serial_basic
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200, safe=False)
        return response


class ViewuseDatumAll(View):
    model_name = "ViewuseDatum"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = ViewuseDatum.actives.all()
        serialized_data = Serializer(data=queryset,
                                     serializer=ViewuseDatumSerializer.serial_basic
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200, safe=False)
        return response
