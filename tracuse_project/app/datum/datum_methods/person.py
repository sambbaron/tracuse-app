from app.element_type.models import ElementType


class DatumObjectPerson(object):
    """On Person datum type"""

    def __init__(self, datum):
        self.datum = datum

    def get_full_name(self):
        """Concatenate first name and last name"""
        element_type = ElementType.objects.get(entity_name="FirstName")
        first_name = self.datum.element_value(element_type).elvalue
        element_type = ElementType.objects.get(entity_name="LastName")
        last_name = self.datum.element_value(element_type).elvalue
        return first_name + " " + last_name

    def get_first_name(self, full_name):
        """Return word at first space"""
        name_partitioned = full_name.partition(" ")
        first_name = name_partitioned[0]
        return first_name

    def get_last_name(self, full_name):
        """Return word(s) after first space"""
        first_name = self.get_first_name(full_name=full_name)
        if first_name == full_name:
            last_name = ""
        else:
            last_name = full_name.replace(first_name + " ", "")
        return last_name
