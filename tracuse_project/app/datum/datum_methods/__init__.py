"""Datum Object Methods by Datum Type"""

from .person import *

class DatumObjectMethodFactory(object):
    """Factory for DatumObject method classes by datum type

    Model Name = "DatumObject" + DatumType.entity_name

    Attributes:
        datum_type_name (string): DatumType.entity_name
    """

    def __new__(cls, datum_object, datum_type_name):
        datum_class_name = "DatumObject" + datum_type_name
        try:
            return globals()[datum_class_name](datum_object)
        except KeyError:
            return None
