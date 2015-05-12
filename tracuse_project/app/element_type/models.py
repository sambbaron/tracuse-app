from django.db import models

from app.common.models import EntityMixin, BaseMixin
from app.element_value.models import ElementValueModel


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

    sort_base_length = 2


class ElementType(EntityMixin):
    """Property types available to Datums

    Has metadata

    Attributes:
        See EntityMixin (includes BaseMixin)
        data_type (integer, fk, required): DataType
            --> string, integer, datetime, etc.
        calc_expression (string):
            Expression in django template language
            Used for defaults and updates
        editable (boolean): Whether value can be edited by user
        datum_types (DatumType set):
            related datum types from ElementDatumType
        datum_objects (DatumObject set):
            related datum objects from ElementDatumObject
    """

    class Meta(EntityMixin.Meta):
        db_table = "element_type"

    element_type_id = models.AutoField(primary_key=True)

    element_data_type = models.ForeignKey("ElementDataType",
                                          db_column="element_data_type_id",
                                          related_name="element_types",
                                          null=False, blank=False
                                          )
    calc_expression = models.CharField(max_length=255,
                                          default="",
                                          null=False, blank=True
                                          )
    editable = models.BooleanField()
    html_element = models.CharField(max_length=25,
                                    default="text",
                                    null=False, blank=False
                                    )
    datum_types = models.ManyToManyField("datum.DatumType",
                                         through="element_type.ElementDatumType",
                                         related_name="+"
                                         )
    datum_objects = models.ManyToManyField("datum.DatumObject",
                                           through="element_type.ElementDatumObject",
                                           related_name="+"
                                           )

    sort_base_length = 3


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
    element_type = models.ForeignKey("ElementType",
                                     db_column="element_type_id",
                                     related_name="element_options",
                                     null=False, blank=False
                                     )

    sort_base_length = 2

    @property
    def sort_parts(self):
        return [self.element_type.sort]


class ElementDatumType(BaseMixin):
    """Default Element Types assigned to Datum Types

    Used at Datum creation - Added to element_value table

    Attributes:
        datum_type_id (integer, fk, pk): DatumType
        element_type_id (integer, fk, pk): ElementType
    """

    class Meta(BaseMixin.Meta):
        db_table = "element_datum_type"
        verbose_name = "Datum Type - Element"
        unique_together = ("datum_type", "element_type")
        index_together = ("datum_type", "element_type")

    # FIXME Django Limitation - composite primary keys
    element_datum_type_id = models.AutoField(primary_key=True)
    datum_type = models.ForeignKey("datum.DatumType",
                                   db_column="datum_type_id",
                                   related_name="element_datum_types",
                                   null=False, blank=False
                                   )
    element_type = models.ForeignKey("ElementType",
                                     db_column="element_type_id",
                                     related_name="datum_element_types",
                                     null=False, blank=False
                                     )

    sort_base_length = -1

    @property
    def sort_parts(self):
        return [self.datum_type.sort, self.element_type.sort]


    def __str__(self):
        return "{} - {}".format(self.datum_type.readable_name, self.element_type.readable_name)


class ElementDatumObject(BaseMixin):
    """Element Types assigned to Datum Objects

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
        db_table = "element_datum_object"
        verbose_name = "Datum Object - Element"
        unique_together = ("datum_object", "element_type")
        index_together = ("datum_object", "element_type")

    # FIXME Django Limitation - composite primary keys
    element_datum_object_id = models.AutoField(primary_key=True)
    datum_object = models.ForeignKey("datum.DatumObject",
                                     db_column="datum_object_id",
                                     related_name="element_datum_objects",
                                     null=False, blank=False
                                     )
    element_type = models.ForeignKey("ElementType",
                                     db_column="element_type_id",
                                     related_name="datum_object_elements",
                                     null=False, blank=False
                                     )

    sort_base_length = -1

    @property
    def sort_parts(self):
        return [self.datum_object.sort, self.element_type.sort]


    def __str__(self):
        return "{} - {}".format(self.datum_object.__str__(), self.element_type.readable_name)

    @property
    def data_type(self):
        return self.element_type.element_data_type.entity_name

    @property
    def element_value_model(self):
        return ElementValueModel(self.data_type)

    @property
    def element_value(self):
        element_value_query = self.element_value_model.objects.filter(element_datum_object=self)
        if element_value_query.exists():
            return element_value_query[0]

    @property
    def get_element_value(self):
        return self.element_value.element_value

    def save(self, *args, **kwargs):
        """Create ElementValue record if it doesn't exist"""
        super().save(*args, **kwargs)
        if not self.element_value:
            new_element_value = self.element_value_model()
            new_element_value.element_datum_object_id = \
                self.element_datum_object_id
