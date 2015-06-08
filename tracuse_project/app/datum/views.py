import json

from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import DatumGroup, DatumType, DatumObject
from .serializers import (DatumGroupSerializer,
                          DatumTypeSerializer,
                          DatumObjectSerializer,
                          DatumObjectDeserializer)
from app.common.serializers import Serializer


class DatumGroupAll(View):
    model_name = "DatumGroup"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = DatumGroup.actives.all()
        serialized_data = Serializer(data=queryset,
                                     serializer=DatumGroupSerializer.serial_datum_types_list
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200, safe=False)
        return response


class DatumTypeAll(View):
    model_name = "DatumType"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = DatumType.actives.all()
        serialized_data = Serializer(data=queryset,
                                     serializer=DatumTypeSerializer.serial_basic
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200, safe=False)
        return response


class DatumObjectAll(View):
    model_name = "DatumObject"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = DatumObject.actives.filter(user=request.user).all()
        serialized_data = Serializer(data=queryset,
                                     serializer=DatumObjectSerializer.serial_datum_elements_list
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200, safe=False)
        return response

    def post(self, request):
        request_data = request.body.decode()
        serialized_data = json.loads(request_data)
        post_data = DatumObjectDeserializer.post_datum(serialized_data, user=request.user)
        if "error" not in post_data:
            response = JsonResponse(post_data, status=201)
        else:
            response = JsonResponse(post_data, status=400)
        return response


class DatumObjectOne(View):
    model_name = "DatumObject"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return DatumObject.objects.get(pk=pk)
        except DatumObject.DoesNotExist:
            raise Http404("Datum Object does not exist.")

    def get(self, request, pk):
        object = self.get_object(pk)
        serialized_data = Serializer(data=object,
                                     serializer=DatumObjectSerializer.serial_datum_elements_objects
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response
