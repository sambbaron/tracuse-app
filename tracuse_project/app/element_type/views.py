from utils.view import ViewAll, ViewOne

from .models import ElementOperator, ElementType, ElementDatumType, ElementDatumObject
from .serializers import (ElementTypeSerializer,
                          ElementOperatorSerializer,
                          ElementDatumTypeSerializer,
                          ElementDatumObjectSerializer)


class ElementTypeAll(ViewAll):
    model = ElementType
    queryset = ElementType.actives.all()
    serializer_class = ElementTypeSerializer
    serializer_template = "serial_related"


class ElementOperatorAll(ViewAll):
    model = ElementOperator
    queryset = ElementOperator.actives.all()
    serializer_class = ElementOperatorSerializer
    serializer_template = "serial_default"


class ElementDatumTypeAll(ViewAll):
    model = ElementDatumType
    queryset = ElementDatumType.actives.all()
    serializer_class = ElementDatumTypeSerializer
    serializer_template = "serial_default"


class ElementDatumObjectAll(ViewAll):
    model = ElementDatumObject
    queryset = ElementDatumObject.actives.all()
    serializer_class = ElementDatumObjectSerializer
    serializer_template = "serial_related"


class ElementDatumObjectOne(ViewOne):
    model = ElementDatumObject
    serializer_class = ElementDatumObjectSerializer
    serializer_template = "serial_related"

    def update_model(self, model_object, request_data):
        element_value_object = model_object.element_value
        element_value_object.elvalue = request_data["element_value"]
        element_value_object.save()
        if element_value_object.elvalue == request_data["element_value"]:
            return model_object
        else:
            return "Error updating element value"
