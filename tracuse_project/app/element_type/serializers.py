from .models import ElementOperator, ElementType, ElementDatumType, ElementDatumObject

from app.utils.serializer import Serializer


class ElementTypeSerializer(Serializer):
    model = ElementType

    @property
    def serial_related(self):
        output = self.serial_default
        output.append(("element_operators",
                       [element_operator.element_operator_id for element_operator in self.obj.element_operators.all()]))
        return output


class ElementOperatorSerializer(Serializer):
    model = ElementOperator


class ElementDatumTypeSerializer(Serializer):
    model = ElementDatumType


class ElementDatumObjectSerializer(Serializer):
    model = ElementDatumObject

    @property
    def serial_default(self):
        element_value = ""
        if self.obj.element_value:
            element_value = self.obj.element_value.elvalue

        output = [
            "element_datum_object_id",
            ("element_datum_type_id", self.obj.element_datum_type.element_datum_type_id),
            ("element_type_id", self.obj.element_type.element_type_id),
            "datum_object_id",
            ("element_name", self.obj.element_type.readable_name),
            ("element_value", element_value)
        ]

        return output

    @property
    def serial_related(self):
        output = self.serial_default
        output.append(("element_datum_type", self.obj.element_datum_type.element_datum_type_id))
        output.append(("element_type", self.obj.element_type.element_type_id))

        return output
