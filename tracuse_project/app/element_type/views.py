from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import ElementType, ElementDatumType
from .serializers import (ElementTypeSerializer,
                          ElementDatumTypeSerializer)
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
