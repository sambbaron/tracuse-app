from .models import DatumGroup, DatumType, DatumObject

from app.utils.serializer import Serializer
from app.element_type.serializers import ElementDatumObjectSerializer
from app.association.serializers import AssociationAllSerializer


class DatumGroupSerializer(Serializer):
    model = DatumGroup

    def serial_related(self):
        output = self.serial_default()
        output.append(("datum_types", [datum_type.datum_type_id for datum_type in self.obj.datum_types.all()]))
        return output


class DatumTypeSerializer(Serializer):
    model = DatumType

    def serial_related(self):
        output = self.serial_default()
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
        output = self.serial_default()

        output.append(("datum_group", self.obj.datum_group.datum_group_id))
        output.append(("datum_type", self.obj.datum_type_id))
        output.append(("elements", [element.element_datum_object_id for element in self.obj.element_datum_objects.all()]))
        output.append(("associations", [association.association_all_id for association in self.obj.all_associations.all()]))

        return output

    def serial_related_object(self):
        """Replace related ids with model objects
        """
        output = self.serial_related()

        elements = []
        for element in self.obj.element_datum_objects.all():
            element_object = ElementDatumObjectSerializer("serial_related").serialize(element)
            elements.append(element_object)
        output.append(("elements", elements))

        associations = []
        for association in self.obj.all_associations.all():
            association_object = AssociationAllSerializer("serial_related").serialize(association)
            associations.append(association_object)
        output.append(("associations", associations))

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
