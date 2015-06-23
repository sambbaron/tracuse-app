from django.db import models
from django.template import Context, Template

from app.common.models import EntityModel, BaseModel
from app.element_value.models import ElementValueMeta

from app.utils.serializer import Serializer


class ElementDataType(EntityModel):
    """Data types available to Elements

    Mapped to element value tables

    FUTURE: Possible presentation formatting properties

    Attributes:
        See EntityModel (includes BaseModel)
        element_class (string, calculated):
            "Element" + data type entity name --> ElementString
        element_table (string, calculated): Element value table name
            "Element" + data type schema name --> element_string
    """

    class Meta(EntityModel.Meta):
        db_table = "element_data_type"
        verbose_name = "Element Data Type"

    element_data_type_id = models.AutoField(primary_key=True)

    sort_base_length = 2


class ElementOperator(EntityModel):
    """Operators assigned to data types

    Used for filtering, correspond to Django queryset lookups

    Attributes:
        See EntityModel (includes BaseModel)
        element_data_type (integer, fk, required): ElementDataType
            --> string, integer, datetime, etc.
        EntityModel.entity_name (string):
            Django field lookup name
        default_operator (boolean):
            Used in ui
    """

    class Meta(EntityModel.Meta):
        db_table = "element_operator"
        verbose_name = "Element Data Type Operator"

    element_operator_id = models.AutoField(primary_key=True)
    element_data_type = models.ForeignKey("ElementDataType",
                                          db_column="element_data_type_id",
                                          related_name="operators",
                                          null=False, blank=False
                                          )
    default_operator = models.BooleanField(default=False,
                                           null=False, blank=False
                                           )
    sort_base_length = 2

    @property
    def sort_parts(self):
        return [self.element_data_type.sort]


class ElementType(EntityModel):
    """Property types available to Datums

    Used to define data presentation and formatting

    Attributes:
        See EntityModel (includes BaseModel)
        element_data_type (integer, fk, required): ElementDataType
            --> string, integer, datetime, etc.
        str_expression (string): Expression in django template language
            that renders to string representation
            use "value" as placeholder for element_value
        editable (boolean): Whether value can be edited by user
        element_view (string): front-end client view name to render element
        data_type_name (string): ElementDataType.entity_name
        element_value_model (ElementValueMeta class):
            uses data_type_name
    """

    class Meta(EntityModel.Meta):
        db_table = "element_type"

    element_type_id = models.AutoField(primary_key=True)

    element_data_type = models.ForeignKey("ElementDataType",
                                          db_column="element_data_type_id",
                                          related_name="element_types",
                                          null=False, blank=False
                                          )
    str_expression = models.CharField(max_length=255,
                                      default="",
                                      null=False, blank=True
                                      )
    editable = models.BooleanField()
    element_view = models.CharField(max_length=25,
                                    default="ElementText",
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

    @property
    def data_type_name(self):
        return self.element_data_type.entity_name

    @property
    def element_value_model(self):
        return ElementValueMeta(self.data_type_name)

    @property
    def element_operators(self):
        return self.element_data_type.operators


class ElementOption(EntityModel):
    """Value options for elements

    Example:
        Action Status - New, Someday, Upcoming, etc.

    Attributes:
        See DefinitionMixin (includes SortActiveMixin)
        element_type_id (integer, fk): ElementType
    """

    class Meta(EntityModel.Meta):
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


class ElementDatumType(EntityModel):
    """Default Element Types assigned to Datum Types

    Used to define data function and logic
    Used at Datum creation - Added to element_value table

    Attributes:
        datum_type_id (integer, fk, pk): DatumType
        element_type_id (integer, fk, pk): ElementType
        calc_expression (string):
            Expression in django template language
            Used for defaults and updates
        primary_view (boolean):
            Whether element_datum_type is included in viewuse
            Temporary solution until more direct assignment of
              elements to viewuses
    """

    class Meta(BaseModel.Meta):
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
    calc_expression = models.CharField(max_length=255,
                                       default="",
                                       null=False, blank=True
                                       )
    primary_view = models.BooleanField(default=False,
                                       null=False, blank=False
                                       )

    sort_base_length = -1

    @property
    def sort_parts(self):
        return [self.datum_type.sort, self.element_type.sort]

    def __str__(self):
        return self.readable_name

    def _get_entity_name(self):
        return self.datum_type.entity_name + \
               self.element_type.entity_name

    def _get_readable_name(self):
        return self.datum_type.readable_name + " - " + \
               self.element_type.readable_name

    def _get_schema_name(self):
        return self.datum_type.schema_name + "_" + \
               self.element_type.schema_name

    def _get_readable_plural_name(self):
        return self.datum_type.readable_plural_name + " - " + \
               self.element_type.readable_plural_name

    def set_entity_name(self):
        self.entity_name = self._get_entity_name()

    def save(self, *args, **kwargs):
        """Set entity names if empty"""

        if self.entity_name is "":
            self.set_entity_name()

        super().save(*args, **kwargs)


class ElementDatumObject(BaseModel):
    """Element Types assigned to Datum Objects

    One-To-One relationship with Element Values tables

    Attributes:
        datum_object_id (integer, fk, pk): DatumObject
        element_type_id (integer, fk, pk): ElementType
        element_datum_type (ElementDatumType object)
        element_value (ElementValue object):
            ElementValue object for ElementType
        get_elvalue (variable):
            'elvalue' column from ElementValue model record
    """

    class Meta(BaseModel.Meta):
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
    def element_datum_type(self):
        element_datum_type = ElementDatumType.objects.filter(
            element_type=self.element_type,
            datum_type=self.datum_object.datum_type
        ).first()
        return element_datum_type

    @property
    def element_value_model(self):
        return self.element_type.element_value_model

    @property
    def element_value(self):
        element_value_object = \
            self.element_value_model \
                .objects.filter(element_datum_object=self).first()

        return element_value_object

    @property
    def get_elvalue(self):
        return self.element_value.elvalue

    def calculated_value(self):
        """Use calc_expression and django template engine
        to return calculated value
        """
        from app.datum.serializers import DatumObjectSerializer

        output = ""
        expression = self.element_datum_type.calc_expression

        if expression:
            template = Template(expression)
            serializer = DatumObjectSerializer(template="serial_element_name_value")
            datum_dict = serializer.serialize(self.datum_object)
            context = Context(datum_dict)
            output = template.render(context)

        return output

    def save(self, *args, **kwargs):
        """Create ElementValue record if it doesn't exist"""
        super().save(*args, **kwargs)
        if not self.element_value:
            new_element_value = self.element_value_model()
            new_element_value.element_datum_object_id = \
                self.element_datum_object_id
