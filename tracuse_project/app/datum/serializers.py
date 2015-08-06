from .models import DatumGroup, DatumType, DatumObject

from app.element_type.serializers import ElementDatumObjectSerializer

from app.utils.serializer import Serializer


class DatumGroupSerializer(Serializer):
    model = DatumGroup

    def serial_related(self):
        output =  self.serial_default()
        output.append(("datum_types", [datum_type.datum_type_id for datum_type in self.obj.datum_types.all()]))
        return output


class DatumTypeSerializer(Serializer):
    model = DatumType

    def serial_related(self):
        output =  self.serial_default()
        output.append(("datum_group", self.obj.datum_group_id))
        return output


class DatumObjectSerializer(Serializer):
    model = DatumObject

    def serial_default(self):
        output = [
            "datum_object_id",
            ("datum_group_id", self.obj.datum_group.datum_group_id),
            "datum_type_id",
            "title"
        ]

        return output

    def serial_related(self):
        output =  self.serial_default()

        output.append(("datum_group", self.obj.datum_group.datum_group_id))
        output.append(("datum_type", self.obj.datum_type_id))
        output.append(("parent_datums", [parent_datum.datum_object_id for parent_datum in self.obj.all_parent_datums.all()]))
        output.append(("child_datums", [child_datum.datum_object_id for child_datum in self.obj.all_child_datums.all()]))
        output.append(("elements", [element.element_datum_object_id for element in self.obj.element_datum_objects.all()]))

        return output

    def serial_elements_object(self):
        """Replace element ids with objects
        """
        output = self.serial_related()

        elements = []
        for element in self.obj.element_datum_objects.all():
            element_object = ElementDatumObjectSerializer("serial_related").serialize(element)
            elements.append(element_object)
        output.append(("elements", elements))

        return output

    def serial_element_name_value(self):
        """Simple elements dictionary for expression evaluation
        """
        output = []

        for element in self.obj.elements:
            element_name = element.element_type.schema_name
            element_value = element.element_value
            if element_value:
                output.append((element_name, element_value.elvalue))

        return output

    def serial_post(self):
        return ["datum_type_id", "user"]