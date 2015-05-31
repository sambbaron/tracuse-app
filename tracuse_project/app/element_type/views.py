import json

from django.http import JsonResponse, HttpResponse, Http404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import ElementOperator, ElementType, ElementDatumType, ElementDatumObject
from .serializers import (ElementTypeSerializer,
                          ElementOperatorSerializer,
                          ElementDatumTypeSerializer,
                          ElementDatumObjectSerializer)
from app.common.serializers import Serializer


class ElementTypeAll(View):
    """Return all element_types"""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = ElementType.actives.all()
        serialized_data = Serializer(data=queryset,
                                     serializer=ElementTypeSerializer.serial_basic,
                                     dict_with_pk=True
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response


class ElementOperatorAll(View):
    """Return all element_types"""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = ElementOperator.actives.all()
        serialized_data = Serializer(data=queryset,
                                     serializer=ElementOperatorSerializer.serial_basic,
                                     dict_with_pk=True
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response


class ElementDatumTypeAll(View):
    """Return all element_types"""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = ElementDatumType.actives.all()
        serialized_data = Serializer(data=queryset,
                                     serializer=ElementDatumTypeSerializer.serial_basic,
                                     dict_with_pk=True
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response


class ElementDatumObjectAll(View):
    """Return all element_datum_objects"""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = ElementDatumObject.actives.all()
        serialized_data = Serializer(data=queryset,
                                     serializer=ElementDatumObjectSerializer.serial_ids_value,
                                     dict_with_pk=True
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response


class ElementDatumObjectOne(View):
    """Return all element_types"""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return ElementDatumObject.objects.get(pk=pk)
        except ElementDatumObject.DoesNotExist:
            raise Http404("Element does not exist.")

    def get(self, request, pk):
        object = self.get_object(pk)
        serialized_data = Serializer(data=object,
                                     serializer=ElementDatumObjectSerializer.serial_ids_value
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response

    def put(self, request, pk):
        object = self.get_object(pk)
        request_data = request.body.decode()
        serialized_data = json.loads(request_data)

        element_value_object = object.element_value
        element_value_object.elvalue = serialized_data["element_value"]
        element_value_object.save()

        if object.element_value.elvalue == serialized_data["element_value"]:
            response_content = ElementDatumObjectSerializer.serial_ids_value(object)
            response = JsonResponse(response_content, status=200)
        else:
            response = HttpResponse("Update error", status=400)
        return response
