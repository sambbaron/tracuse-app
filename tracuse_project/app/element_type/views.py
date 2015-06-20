from utils.view import ViewAll, ViewOne

from .models import ElementOperator, ElementType, ElementDatumType, ElementDatumObject
from .serializers import (ElementTypeSerializer,
                          ElementOperatorSerializer,
                          ElementDatumTypeSerializer,
                          ElementDatumObjectSerializer)


class ElementTypeAll(ViewAll):
    model = ElementType
    queryset = ElementType.actives.all()
    serializer=ElementTypeSerializer.serial_related


class ElementOperatorAll(ViewAll):
    model = ElementOperator
    queryset = ElementOperator.actives.all()
    serializer=ElementOperatorSerializer.serial_basic


class ElementDatumTypeAll(ViewAll):
    model = ElementDatumType
    queryset = ElementDatumType.actives.all()
    serializer=ElementDatumTypeSerializer.serial_basic


class ElementDatumObjectAll(ViewAll):
    model = ElementDatumObject
    queryset = ElementDatumObject.actives.all()
    serializer=ElementDatumObjectSerializer.serial_related


class ElementDatumObjectOne(ViewOne):
    model = ElementDatumObject
    serializer=ElementDatumObjectSerializer.serial_related

    def update_save(self, model_object, request_data, request_object):
        element_value_object = model_object.element_value
        element_value_object.elvalue = request_data["element_value"]
        element_value_object.save()
        if element_value_object.elvalue == request_data["element_value"]:
            return model_object
        else:
            return "Error updating element value"