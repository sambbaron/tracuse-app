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

    def serial_related(self):
        """All properties with relations
        """
        datum_types = [datum_type.datum_type_id for datum_type in self.datum_types.all()]
        output = self.serial_basic()
        output["datum_types"] = datum_types
        return output

    DatumGroup.serial_related = serial_related


class DatumTypeSerializer(DatumType):
    class Meta:
        abstract = True

    def serial_basic(self):
        """All properties"""
        output = serialize_all(self.__class__, self)
        return output

    DatumType.serial_basic = serial_basic

    def serial_related(self):
        """All properties with relations
        """
        output = self.serial_basic()
        output["datum_group"] = self.datum_group_id
        return output

    DatumType.serial_related = serial_related


class DatumObjectSerializer(DatumObject):
    class Meta:
        abstract = True

    def serial_basic(self):
        """All properties"""
        output = {
            "datum_object_id": self.datum_object_id,
            "datum_group_id": self.datum_group.datum_group_id,
            "datum_type_id": self.datum_type_id,
            "headline": self.headline,
        }
        return output

    DatumObject.serial_basic = serial_basic

    def serial_related(self):
        """All properties with relations
        """
        output = self.serial_basic()

        output["datum_group"] = self.datum_group.datum_group_id
        output["datum_type"] = self.datum_type_id
        output["parent_datums"] = [parent_datum.datum_object_id for parent_datum in self.all_parent_datums.all()]
        output["child_datums"] = [child_datum.datum_object_id for child_datum in self.all_child_datums.all()]
        output["elements"] = [element.element_datum_object_id for element in self.element_datum_objects.all()]

        return output

    DatumObject.serial_related = serial_related

    def serial_elements_object(self):
        """Replace element ids with objects
        """
        output = self.serial_related()

        elements = []
        for element in self.element_datum_objects.all():
            element_object = ElementDatumObjectSerializer.serial_related(element)
            elements.append(element_object)

        output["elements"] = elements

        return output

    DatumObject.serial_elements_object = serial_elements_object

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


class DatumObjectDeserializer(object):
    @staticmethod
    def post_datum(data, user, pk=None):
        response = {"error": "unknown"}

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
