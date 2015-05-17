from .models import ElementType, ElementDatumType, ElementDatumObject
from app.common.serializers import Serializer

class ElementTypeSerializer(ElementType, Serializer):
    class Meta:
        abstract = True

    def serial_basic(self):
        """Element types with all properties

        Returns:
            Key: element_type_id
            Value: Property Dictionary
        """
        output = {}
        for field in ElementType._meta.fields:
            column_name = field.get_attname_column()[1]
            output[column_name] = getattr(self, column_name)

        return output

    ElementType.serial_basic = serial_basic


class ElementDatumObjectSerializer(ElementDatumObject):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
