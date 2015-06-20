import json

from django.http import JsonResponse, Http404
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
from utils.serializer import Serializer
from utils.model import update_model


class ViewuseObjectAll(View):
    model_name = "ViewuseObject"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = ViewuseObject.actives.filter(Q(user=request.user) | Q(user=None)).all()
        serialized_data = Serializer(data=queryset,
                                     serializer=ViewuseObjectSerializer.serial_related
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
                                     serializer=ViewuseObjectSerializer.serial_related
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response

    def put(self, request, pk):
        object = self.get_object(pk)
        request_data = request.body.decode()
        serialized_data = json.loads(request_data)

        field_list = [
            ("readable_name",),
            ("viewuse_arrangement_id",),
            ("viewuse_datum_id",),
            ("filter_json", "json"),
        ]

        model_save = update_model(object, field_list, serialized_data)
        if type(model_save) == str:
            response = JsonResponse(model_save, status=400, safe=False)
        else:
            serialized_data = Serializer(data=model_save,
                                         serializer=ViewuseObjectSerializer.serial_related
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
