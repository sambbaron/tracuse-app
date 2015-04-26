from django.db import models

from common.mixins import EntityMixin
from datum.models import DatumType

class ElementDataType(EntityMixin):
    """Data types available to Elements

    Mapped to element value tables and presentation formatting

    Attributes:
        element_class (string, calculated):
            "Element" + data type entity name --> ElementString
        element_table (string, calculated): Element value table name
            "Element" + data type schema name --> element_string
        html_tag (string): HTML form input tag for data type
    """

    class Meta(EntityMixin.Meta):
        db_table = "element_data_type"

    element_data_type_id = models.AutoField(primary_key=True)

    html_tag = models.CharField(max_length=10)

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

    data_type = models.ForeignKey("ElementDataType",
                                  db_column="data_type_id",
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
    EntityMixin.entity_name.unique = False
    element_type = models.ForeignKey("ElementType",
                                     db_column="element_type_id",
                                     null=False, blank=False
                                     )


class ElementTypeDatumType(EntityMixin):
    """Default Element Types assigned to Datum Types

    Used at Datum creation - Added to element_value table

        Attributes:
            datum_type_id (integer, fk, pk): DatumType
            element_type_id (integer, fk, pk): ElementType
    """

    class Meta(EntityMixin.Meta):
        db_table = "element_type_datum_type"

    datum_type = models.ForeignKey("DatumType",
                                   db_column="datum_type_id",
                                   primary_key=True
                                   )
    element_type = models.ForeignKey("ElementType",
                                     db_column="element_type_id",
                                     primary_key=True
                                     )

