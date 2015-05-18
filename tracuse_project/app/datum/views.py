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
    """Return all datum_groups"""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = DatumGroup.actives.all()
        serialized_data = Serializer(data=queryset,
                                     serializer=DatumGroupSerializer.serial_basic,
                                     dict_with_pk=True
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response


class DatumTypeAll(View):
    """Return all datum_types"""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = DatumType.actives.all()
        serialized_data = Serializer(data=queryset,
                                     serializer=DatumTypeSerializer.serial_basic,
                                     dict_with_pk=True
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response

class DatumObjectAll(View):
    """List all datum_objects, or create a new datum_object.
    """

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        # if obj.user == request.user

    def get(self, request):
        queryset = DatumObject.actives.filter(user=request.user).all()
        serialized_data = Serializer(data=queryset,
                                     serializer=DatumObjectSerializer.serial_datum_all,
                                     dict_with_pk=True
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
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
    """Retrieve, update or delete a datum_object instance.
    """

    @login_required
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
                                     serializer=DatumObjectSerializer.serial_datum_all
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response

    def put(self, request, pk):
        request_data = request.body.decode()
        serialized_data = json.loads(request_data)
        post_data = post_datum_object(serialized_data)
        if type(post_data) == DatumObject:
            response = JsonResponse(post_data, status=200)
        else:
            response = HttpResponse(post_data, status=400)
        return response

    def delete(self, request, pk):
        datum_object = self.get_object(pk)
        datum_object.delete()
        return HttpResponse(status=204)
