
from .models import DatumObject

class DatumObjectSerializer(DatumObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def element_name_value(self):
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