from .models import DatumGroup, DatumType, DatumObject

from app.element_type.serializers import ElementDatumObjectSerializer

from app.utils.serializer import Serializer


class DatumGroupSerializer(Serializer):
    model = DatumGroup

    @property
    def serial_related(self):
        output = self.serial_default
        output["datum_types"] = [datum_type.datum_type_id for datum_type in self.obj.datum_types.all()]
        return output


class DatumTypeSerializer(Serializer):
    model = DatumType

    @property
    def serial_related(self):
        output = self.serial_default
        output["datum_group"] = self.obj.datum_group_id
        return output


class DatumObjectSerializer(Serializer):
    model = DatumObject
    
    @property
    def serial_default(self):
        output = {
            "datum_object_id": self.obj.datum_object_id,
            "datum_group_id": self.obj.datum_group.datum_group_id,
            "datum_type_id": self.obj.datum_type_id,
            "headline": self.obj.headline,
        }

        return output

    @property
    def serial_related(self):
        output = self.serial_default

        output["datum_group"] = self.obj.datum_group.datum_group_id
        output["datum_type"] = self.obj.datum_type_id
        output["parent_datums"] = [parent_datum.datum_object_id for parent_datum in self.obj.all_parent_datums.all()]
        output["child_datums"] = [child_datum.datum_object_id for child_datum in self.obj.all_child_datums.all()]
        output["elements"] = [element.element_datum_object_id for element in self.obj.element_datum_objects.all()]

        return output

    @property
    def serial_elements_object(self):
        """Replace element ids with objects
        """
        output = self.serial_related

        elements = []
        for element in self.obj.element_datum_objects.all():
            element_object = ElementDatumObjectSerializer(data=element, template="serial_related").serialize
            elements.append(element_object)
        output["elements"] = elements

        return output

    @property
    def serial_element_name_value(self):
        """Simple elements dictionary for expression evaluation
        """
        output = {}

        for element in self.obj.elements:
            element_name = element.element_type.schema_name
            element_value = element.element_value
            if element_value:
                output[element_name] = element_value.elvalue

        return output