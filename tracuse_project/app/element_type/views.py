from utils.view import ViewAll, ViewOne

from .models import (ElementOperator,
                     ElementType,
                     ElementDatumType,
                     ElementDatumObject,
                     ElementOption,
                     ElementDataType)
from .serializers import (ElementTypeSerializer,
                          ElementOperatorSerializer,
                          ElementDatumTypeSerializer,
                          ElementDatumObjectSerializer,
                          ElementOptionSerializer,
                          ElementDataTypeSerializer)


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
    deserializer_template = "serial_update"

    def update_model(self, model_object, request_data):
        """ Override ViewBase update_model
        Get ElementValue model object and set deserializer model
        """
        pk = model_object.pk

        element_value_object = model_object.element_value
        self.deserializer.model = element_value_object.__class__
        element_value_save = self.deserializer.deserialize(element_value_object, request_data)

        if type(element_value_save) == str:
            return element_value_save
        else:
            return self.get_object(pk)

class ElementOptionAll(ViewAll):
    model = ElementOption
    queryset = ElementOption.actives.all()
    serializer_class = ElementOptionSerializer

class ElementDataTypeAll(ViewAll):
    model = ElementDataType
    queryset = ElementDataType.objects.all()
    serializer_class = ElementDataTypeSerializer
