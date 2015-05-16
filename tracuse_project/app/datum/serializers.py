from .models import DatumObject


class DatumObjectSerializer(DatumObject):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def serial_basic(self):
        output = {
            "datum_object_id": self.datum_object_id,
            "datum_type": self.datum_type.datum_type_id
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

        parent_datums = [parent_datum.datum_object_id for parent_datum in self.all_parent_datums.all()]
        child_datums = [child_datum.datum_object_id for child_datum in self.all_child_datums.all()]

        output = {
            "datum_object_id": self.datum_object_id,
            "datum_group": self.datum_group.datum_group_id,
            "datum_type": self.datum_type_id,
            "parent_datums": parent_datums,
            "child:datums": child_datums,
            "element": self.serial_element_name_value()
        }
        return output

    DatumObject.serial_element_name_value = serial_element_name_value

class DatumObjectDeserializer(object):

    @staticmethod
    def post_datum(data, user, pk=None):
        response = None

        if pk is None:
            new_obj = DatumObject.objects.create(
                user=user,
                datum_type_id=data["datum_type"]
            )
            response = DatumObjectSerializer.serial_basic(new_obj)
        else:
            pass

        return response
