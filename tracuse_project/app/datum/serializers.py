from .models import DatumGroup, DatumType, DatumObject

from app.element_type.serializers import ElementDatumObjectSerializer

from app.common.serializers import serialize_all


class DatumGroupSerializer(DatumGroup):
    class Meta:
        abstract = True

    def serial_basic(self):
        """All properties"""
        output = serialize_all(self.__class__, self)
        return output

    DatumGroup.serial_basic = serial_basic


class DatumTypeSerializer(DatumType):
    class Meta:
        abstract = True

    def serial_basic(self):
        """All properties"""
        output = serialize_all(self.__class__, self)
        return output

    DatumType.serial_basic = serial_basic


class DatumObjectSerializer(DatumObject):
    class Meta:
        abstract = True

    def serial_basic(self):
        output = {
            "datum_object_id": self.datum_object_id,
            "datum_type_id": self.datum_type.datum_type_id
        }
        return output

    def serial_element_name_value(self):
        """Return elements for expression evaluation

        Returns:
            Dictionary:
                Key: element_type.schema_name
                Value: element_value.elvalue
        """
        output = {}

        for element in self.elements:
            element_name = element.element_type.schema_name
            element_value = element.element_value
            if element_value:
                output[element_name] = element_value.elvalue

        return output

    DatumObject.serial_element_name_value = serial_element_name_value

    def serial_datum_all(self):
        """Datums with all properties

        Returns:
            Key: datum_object_id
            Value: Property Dictionary
        """

        parent_datums = [parent_datum.datum_object_id for parent_datum in self.all_parent_datums.all()]
        child_datums = [child_datum.datum_object_id for child_datum in self.all_child_datums.all()]
        elements = [element.element_datum_object_id for element in self.element_datum_objects.all()]

        output = {
            "datum_object_id": self.datum_object_id,
            "datum_group_id": self.datum_group.datum_group_id,
            "datum_type_id": self.datum_type_id,
            "datum_type_name": self.datum_type.readable_name,
            "headline": self.headline,
            "parent_datums": parent_datums,
            "child_datums": child_datums,
            "elements": elements
        }

        return output

    DatumObject.serial_datum_all = serial_datum_all


class DatumObjectDeserializer(object):
    @staticmethod
    def post_datum(data, user, pk=None):
        response = {"error":"unknown"}

        if pk is None:
            try:
                new_obj = DatumObject.objects.create(
                    user=user,
                    datum_type_id=data["datum_type_id"]
                )
                response = DatumObjectSerializer.serial_basic(new_obj)
            except KeyError:
                response = {"error": "Data post error"}
        else:
            pass

        return response
