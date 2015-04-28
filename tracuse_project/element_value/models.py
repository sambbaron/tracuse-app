from django.db import models

from common.mixins import BaseMixin


class ElementValueMixin(BaseMixin):
    """Common columns for ElementValue models

    Type-specific tables
    Mapped to ElementDataType model

    Attributes:
        See BaseMixin
        datum_object_id (integer, fk, required): DatumObject
         element_type_datum_object (integer, fk, required):
            ElementTypeDatumObject --> One-To-One
        element_option_id (integer, fk, nullable): ElementOption
    """

    # FIXME Django Limitation - Can't create custom Meta property for db_table expression
    class Meta(BaseMixin.Meta):
        abstract = True

    element_type_datum_object = \
        models.OneToOneField("element_type.ElementTypeDatumObject",
                             db_column="element_type_datum_object_id",
                             null=False, blank=False
                             )
    element_option = models.ForeignKey("element_type.ElementOption",
                                       db_column="element_option_id",
                                       null=True, blank=True
                                       )


class ElementValueString(ElementValueMixin):
    """String-Type Element Values

    Attributes:
        See ElementValueMixin (includes BaseMixin)
        element_value (string, nullable)
    """

    class Meta(ElementValueMixin.Meta):
        db_table = "element_value_string"

    element_value_string_id = models.AutoField(primary_key=True)
    element_value = models.CharField(max_length=150,
                                     null=True, blank=True
                                     )


class ElementValueTextData(ElementValueMixin):
    """Long text data Element Values

    Attributes:
        See ElementValueMixin (includes BaseMixin)
        element_value (text, nullable)
    """

    class Meta(ElementValueMixin.Meta):
        db_table = "element_value_textdata"

    element_value_textdata_id = models.AutoField(primary_key=True)
    element_value = models.TextField(null=True, blank=True
                                     )


class ElementValueBoolean(ElementValueMixin):
    """Boolean-type Element Values

    Attributes:
        See ElementValueMixin (includes BaseMixin)
        element_value (boolean)
    """

    class Meta(ElementValueMixin.Meta):
        db_table = "element_value_boolean"

    element_value_boolean_id = models.AutoField(primary_key=True)
    element_value = models.BooleanField()


class ElementValueDatetime(ElementValueMixin):
    """Datetime-Type Element Values

    Attributes:
        See ElementValueMixin (includes BaseMixin)
        element_value (datetime, nullable)
    """

    class Meta(ElementValueMixin.Meta):
        db_table = "element_value_datetime"

    element_value_datetime_id = models.AutoField(primary_key=True)
    element_value = models.DateTimeField(null=True, blank=True
                                         )


class ElementValueDecimal(ElementValueMixin):
    """Decimal-Type Element Values

    Attributes:
        See ElementValueMixin (includes BaseMixin)
        element_value (decimal, nullable)
    """

    class Meta(ElementValueMixin.Meta):
        db_table = "element_value_decimal"

    element_value_decimal_id = models.AutoField(primary_key=True)
    element_value = models.DecimalField(max_digits=10, decimal_places=2,
                                        null=True, blank=True
                                        )


class ElementValueBinary(ElementValueMixin):
    """Binary/Blob-Type Element Values

    Attributes:
        See ElementValueMixin (includes BaseMixin)
        element_value (binary, nullable)
    """

    class Meta(ElementValueMixin.Meta):
        db_table = "element_value_binary"

    element_value_binary_id = models.AutoField(primary_key=True)
    element_value = models.BinaryField(null=True, blank=True
                                       )