from django.db import models

from common.mixins import EntityMixin, BaseMixin


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

    element_data_type_id = models.AutoField(primary_key=True)

    @property
    def element_class(self):
        return "Element" + self.entity_name

    @property
    def element_table(self):
        return "element_" + self.schema_name


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
        unique_together = ("datum_type", "element_type")
        index_together = ("datum_type", "element_type")

    # FIXME Django Limitation - composite primary keys
    element_type_datum_type_id = models.AutoField(primary_key=True)
    datum_type = models.ForeignKey("datum.DatumType",
                                   db_column="datum_type_id",
                                   related_name="element_types",
                                   null=False, blank=False
                                   )
    element_type = models.ForeignKey("ElementType",
                                     db_column="element_type_id",
                                     related_name="datum_types",
                                     null=False, blank=False
                                     )

