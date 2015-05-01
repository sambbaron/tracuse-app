from django.db import models

from utils.mixins import EntityMixin, BaseMixin
from components.element_value.models import ElementValueModel


class ElementDataType(EntityMixin):
    """Data types available to Elements

    Mapped to element value tables

    FUTURE: Possible presentation formatting properties

    Attributes:
        element_class (string, calculated):
            "Element" + data type entity name --> ElementString
        element_table (string, calculated): Element value table name
            "Element" + data type schema name --> element_string
    """

    class Meta(EntityMixin.Meta):
        db_table = "element_data_type"
        verbose_name = "Element Data Type"

    element_data_type_id = models.AutoField(primary_key=True)


class ElementType(EntityMixin):
    """Property types available to Datums

    Has metadata

    Attributes:
        See EntityMixin (includes BaseMixin)
        data_type (integer, fk, required): DataType
            --> string, integer, datetime, etc.
        default_expression (string): Default expression
        editable (boolean): Whether value can be edited by user
    """

    class Meta(EntityMixin.Meta):
        db_table = "element_type"

    element_type_id = models.AutoField(primary_key=True)

    element_data_type = models.ForeignKey("ElementDataType",
                                          db_column="element_data_type_id",
                                          related_name="element_types",
                                          null=False, blank=False
                                          )
    default_expression = models.CharField(max_length=255,
                                          null=True, blank=True
                                          )
    editable = models.BooleanField()


class ElementOption(EntityMixin):
    """Value options for elements

    Example:
        Action Status - New, Someday, Upcoming, etc.

    Attributes:
        See DefinitionMixin (includes SortActiveMixin)
        element_type_id (integer, fk): ElementType
    """

    class Meta(EntityMixin.Meta):
        db_table = "element_option"
        verbose_name = "Element Option"

    element_option_id = models.AutoField(primary_key=True)
    # FIXME Django Limitation - Can't override field property from Abstract Mixin Class
    # FIXME Django Limitation - Change 'entity_name' unique false
    element_type = models.ForeignKey("ElementType",
                                     db_column="element_type_id",
                                     related_name="element_options",
                                     null=False, blank=False
                                     )


class ElementTypeDatumType(BaseMixin):
    """Default Element Types assigned to Datum Types

    Used at Datum creation - Added to element_value table

    Attributes:
        datum_type_id (integer, fk, pk): DatumType
        element_type_id (integer, fk, pk): ElementType
    """

    class Meta(BaseMixin.Meta):
        db_table = "element_type_datum_type"
        verbose_name = "Element Type - Datum Type"
        unique_together = ("datum_type", "element_type")
        index_together = ("datum_type", "element_type")

    # FIXME Django Limitation - composite primary keys
    element_type_datum_type_id = models.AutoField(primary_key=True)
    datum_type = models.ForeignKey("datum.DatumType",
                                   db_column="datum_type_id",
                                   related_name="element_types_datum_types",
                                   null=False, blank=False
                                   )
    element_type = models.ForeignKey("ElementType",
                                     db_column="element_type_id",
                                     related_name="datum_types_element_types",
                                     null=False, blank=False
                                     )

    def __str__(self):
        return "{} - {}".format(self.datum_type.readable_name, self.element_type.readable_name)


class ElementTypeDatumObject(BaseMixin):
    """Element Types assigned to Datum Types

    One-To-One relationship with Element Values tables

    Attributes:
        datum_object_id (integer, fk, pk): DatumObject
        element_type_id (integer, fk, pk): ElementType
        element_value (ElementValue object):
            ElementValue objects for ElementType
        get_element_value (variable):
            'element_value' column from ElementValue model record
    """

    class Meta(BaseMixin.Meta):
        db_table = "element_type_datum_object"
        verbose_name = "Element Type - Datum Object"
        unique_together = ("datum_object", "element_type")
        index_together = ("datum_object", "element_type")

    # FIXME Django Limitation - composite primary keys
    element_type_datum_object_id = models.AutoField(primary_key=True)
    datum_object = models.ForeignKey("datum.DatumObject",
                                     db_column="datum_object_id",
                                     related_name="element_types_datum_objects",
                                     null=False, blank=False
                                     )
    element_type = models.ForeignKey("ElementType",
                                     db_column="element_type_id",
                                     related_name="datum_objects_element_types",
                                     null=False, blank=False
                                     )

    @property
    def element_value(self):
        data_type_name = self.element_type.element_data_type.entity_name
        element_value_model = ElementValueModel(data_type_name)
        element_value_record = element_value_model.objects.get(element_type_datum_object=self)
        return element_value_record

    @property
    def get_element_value(self):
        return self.element_value.element_value

    def __str__(self):
        return "{} - {}".format(self.datum_object.__str__(), self.element_type.readable_name)