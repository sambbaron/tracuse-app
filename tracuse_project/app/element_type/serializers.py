from .models import (ElementOperator,
                     ElementType,
                     ElementDatumType,
                     ElementDatumObject,
                     ElementOption,
                     ElementDataType)

from app.utils.serializer import Serializer


class ElementTypeSerializer(Serializer):
    model = ElementType

    def serial_related(self):
        output = self.serial_default()
        output.append(("element_data_type", self.obj.element_data_type.schema_name))
        output.append(("element_operators",
                       [element_operator.element_operator_id for element_operator in self.obj.element_operators.all()]))
        output.append(("element_options",
                       [element_option.element_option_id for element_option in self.obj.element_options.all()]))

        return output


class ElementOperatorSerializer(Serializer):
    model = ElementOperator


class ElementDatumTypeSerializer(Serializer):
    model = ElementDatumType


class ElementDatumObjectSerializer(Serializer):
    model = ElementDatumObject

    def serial_default(self):
        element_value = ""
        if self.obj.element_value:
            element_value = self.obj.element_value.elvalue

        output = [
            "element_datum_object_id",
            ("element_datum_type_id", self.obj.element_datum_type.element_datum_type_id),
            ("element_type_id", self.obj.element_type.element_type_id),
            ("element_data_type", self.obj.element_type.element_data_type.schema_name),
            "datum_object_id",
            ("element_name", self.obj.element_type.readable_name),
            ("element_value", element_value)
        ]

        return output

    def serial_related(self):
        output = self.serial_default()
        output.append(("element_datum_type", self.obj.element_datum_type.element_datum_type_id))
        output.append(("element_type", self.obj.element_type.element_type_id))

        return output

    def serial_update(self):
        return [
            ("elvalue", self.obj.element_value)
        ]


class ElementOptionSerializer(Serializer):
    model = ElementOption


class ElementDataTypeSerializer(Serializer):
    model = ElementDataType
