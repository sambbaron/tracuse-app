from django.db import models
from django.template import Context, Template

from app.common.models import BaseMixin


class ElementValueModel(object):
    """Factory class for ElementValue models

    Model Name = "ElementValue" + ElementDataType.entity_name

    Attributes:
        data_type_name (string): ElementDataType.entity_name
    """

    def __new__(cls, data_type_name):
        value_model_name = "ElementValue" + data_type_name
        try:
            return globals()[value_model_name]
        except KeyError:
            raise NameError("{} model class does not exist".format(value_model_name))


class ElementValueMixin(BaseMixin):
    """Common columns for ElementValue models

    Type-specific tables
    Mapped to ElementDataType model

    Attributes:
        See BaseMixin
        datum_object_id (integer, fk, required): DatumObject
         element_datum_object (integer, fk, required):
            ElementDatumObject --> One-To-One
        element_option_id (integer, fk, optional): ElementOption
        datum_object (DatumObject):
        element_type (ElementType):
    """

    # FIXME Django Limitation - Can't create custom Meta property for db_table expression
    class Meta(BaseMixin.Meta):
        abstract = True
        verbose_name = "Element Value"

    element_datum_object = \
        models.OneToOneField("element_type.ElementDatumObject",
                             db_column="element_datum_object_id",
                             null=False, blank=False
                             )
    element_option = models.ForeignKey("element_type.ElementOption",
                                       db_column="element_option_id",
                                       null=True, blank=True
                                       )

    sort_base_length = -1

    @property
    def sort_parts(self):
        return [self.element_datum_object.sort]


    def __str__(self):
        """Use ElementDatumType.str_expression with django template engine"""
        output = ""
        expression = self.element_type.str_expression

        if expression:
            template = Template(expression)
            context = Context({"value": self.element_value})
            output = template.render(context)

        if not output or output is None:
            output = str(self.element_value)

        return output

    @property
    def datum_object(self):
        return self.element_datum_object.datum_object

    @property
    def element_type(self):
        return self.element_datum_object.element_type


class ElementValueString(ElementValueMixin):
    """String-Type Element Values

    Attributes:
        See ElementValueMixin (includes BaseMixin)
        element_value (string, optional)
    """

    class Meta(ElementValueMixin.Meta):
        db_table = "element_value_string"
        default_related_name = "element_value_string"

    element_value_string_id = models.AutoField(primary_key=True)
    element_value = models.CharField(max_length=150,
                                     default="",
                                     null=False, blank=True
                                     )


class ElementValueTextData(ElementValueMixin):
    """Long text data Element Values

    Attributes:
        See ElementValueMixin (includes BaseMixin)
        element_value (text, optional)
    """

    class Meta(ElementValueMixin.Meta):
        db_table = "element_value_textdata"
        default_related_name = "element_value_textdata"

    element_value_textdata_id = models.AutoField(primary_key=True)
    element_value = models.TextField(default="",
                                     null=False, blank=True
                                     )


class ElementValueBoolean(ElementValueMixin):
    """Boolean-type Element Values

    Attributes:
        See ElementValueMixin (includes BaseMixin)
        element_value (boolean)
    """

    class Meta(ElementValueMixin.Meta):
        db_table = "element_value_boolean"
        default_related_name = "element_value_boolean"

    element_value_boolean_id = models.AutoField(primary_key=True)
    element_value = models.BooleanField(default=False)


class ElementValueDatetime(ElementValueMixin):
    """Datetime-Type Element Values

    Attributes:
        See ElementValueMixin (includes BaseMixin)
        element_value (datetime, optional)
    """

    class Meta(ElementValueMixin.Meta):
        db_table = "element_value_datetime"
        default_related_name = "element_value_datetime"

    element_value_datetime_id = models.AutoField(primary_key=True)
    element_value = models.DateTimeField(null=True, blank=True
                                         )


class ElementValueDecimal(ElementValueMixin):
    """Decimal-Type Element Values

    Attributes:
        See ElementValueMixin (includes BaseMixin)
        element_value (decimal, optional)
    """

    class Meta(ElementValueMixin.Meta):
        db_table = "element_value_decimal"
        default_related_name = "element_value_decimal"

    element_value_decimal_id = models.AutoField(primary_key=True)
    element_value = models.DecimalField(max_digits=10, decimal_places=2,
                                        null=True, blank=True
                                        )


class ElementValueBinary(ElementValueMixin):
    """Binary/Blob-Type Element Values

    Attributes:
        See ElementValueMixin (includes BaseMixin)
        element_value (binary, optional)
    """

    class Meta(ElementValueMixin.Meta):
        db_table = "element_value_binary"
        default_related_name = "element_value_binary"

    element_value_binary_id = models.AutoField(primary_key=True)
    element_value = models.BinaryField(null=True, blank=True
                                       )
