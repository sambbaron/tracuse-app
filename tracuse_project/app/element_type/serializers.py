from .models import ElementType, ElementDatumType, ElementDatumObject

from app.common.serializers import serialize_all


class ElementTypeSerializer(ElementType):
    class Meta:
        abstract = True

    def serial_basic(self):
        """All properties"""
        output = serialize_all(self.__class__, self)
        return output

    ElementType.serial_basic = serial_basic


class ElementDatumTypeSerializer(ElementDatumType):
    class Meta:
        abstract = True

    def serial_basic(self):
        """All properties"""
        output = serialize_all(self.__class__, self)
        return output

    ElementDatumType.serial_basic = serial_basic


class ElementDatumObjectSerializer(ElementDatumObject):
    class Meta:
        abstract = True

    def serial_ids_value(self):
        """Elements with all ids and value

        Returns:
            Key: datum_object_id
            Value: Property Dictionary
        """
        element_value = ""
        if self.element_value:
            element_value = self.element_value.elvalue

        output = {
            "element_datum_object_id": self.element_datum_object_id,
            "element_datum_type_id": self.element_datum_type.element_datum_type_id,
            "element_type_id": self.element_type.element_type_id,
            "element_value": element_value
        }

        return output

    ElementDatumObject.serial_ids_value = serial_ids_value
