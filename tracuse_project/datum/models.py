from django.db import models

from django.contrib.auth.models import User

from common.mixins import EntityMixin, BaseMixin
from element_type.models import ElementType


class DatumGroup(EntityMixin):
    """Collection of Datum Types

    Has common functional uses

    Attributes:
        See EntityMixin (includes BaseMixin)
    """

    class Meta(EntityMixin.Meta):
        db_table = "datum_group"
        verbose_name = "Datum Group"

    datum_group_id = models.AutoField(primary_key=True)


class DatumType(EntityMixin):
    """Type of Datum Objects

    Has common functional use and properties (elements)

    Attributes:
        See EntityMixin (includes BaseMixin)
        datum_group_id (integer, fk, required): DatumGroup
        repr_expression (string): Expression that results in
            representation string, can reference element types
            --> !name + " " + !description
    """

    class Meta(EntityMixin.Meta):
        db_table = "datum_type"
        verbose_name = "Datum Type"

    datum_type_id = models.AutoField(primary_key=True)

    datum_group = models.ForeignKey("DatumGroup",
                                    db_column="datum_group_id",
                                    null=False, blank=False,
                                    db_index=True
                                    )
    repr_expression = models.CharField(max_length=255,
                                       null=False, blank=False
                                       )
    parent_associations_all = models.ManyToManyField("self",
                                                     related_name="child_associations_all",
                                                     through="association.AssociationAll",
                                                     symmetrical=False
                                                     )


class DatumObject(BaseMixin):
    """Primary personal information data object

    Node/Vertex in graph
    Has Datum Type which defines properties (elements)

    Attributes:
        See BaseMixin
        user_id (integer, fk, required): User
        datum_type_id (integer, fk, required): DatumType
        datum_group (DatumGroup):
        default_element_types (list):
            ElementTypes from ElementTypeDatumType
        assigned_element_types (list):
            ElementTypes from ElementTypeDatumObject
        element_values_objects (list):
            ElementValue objects

    Methods:
        element_value (ElementValue):
            Return single ElementValue object for selected element type
        get_element_value (variable):
            Return element value for selected element type
        element_values_dict (dict):
            Return element values for multiple element types
    """

    class Meta(BaseMixin.Meta):
        db_table = "datum_object"
        verbose_name = "Datum"

    datum_object_id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User,
                             db_column="user_id",
                             related_name="datum_objects",
                             null=False, blank=False,
                             db_index=True
                             )
    datum_type = models.ForeignKey("DatumType",
                                   db_column="datum_type_id",
                                   related_name="datum_objects",
                                   null=False, blank=False,
                                   db_index=True
                                   )
    parent_associations_adjacent = \
        models.ManyToManyField("self",
                               related_name="child_associations_adjacent",
                               through="association.AssociationAdjacent",
                               symmetrical=False
                               )
    parent_associations_all = \
        models.ManyToManyField("self",
                               related_name="child_associations_all",
                               through="association.AssociationAll",
                               symmetrical=False
                               )

    @property
    def datum_group(self):
        return self.datum_type.datum_group

    @property
    def default_element_types(self):
        element_types = []
        for datum_type_element_type in self.datum_type.element_types_datum_types.all():
            related_element_type = datum_type_element_type.element_type
            element_types.append(related_element_type)
        return element_types

    @property
    def assigned_element_types(self):
        element_types = []
        for datum_object_element_type in self.element_types_datum_objects.all():
            related_element_type = datum_object_element_type.element_type
            element_types.append(related_element_type)
        return element_types

    def element_value(self, element_type_object):
        """Retrieve Single Element Value Object for Element Type

        Args:
            element_type (ElementType object)

        Return:
            ElementValue value: data type depends on element type
        """

        if element_type_object not in self.assigned_element_types:
            return

        # Lookup ElementTypeDatumType object for association
        element_type_datum_object = self.element_types_datum_objects. \
            get(element_type=element_type_object)
        return element_type_datum_object.element_value


    def get_element_value(self, element_type_object):
        element_value_object = self.element_value(element_type_object)
        return element_value_object.element_value


    def element_values_dict(self, element_type_list=None):
        """Retrieve Multiple Element Values Objects for Datum Object

        Args:
            element_type_list (ElementType objects list, optional):
                Specific element types to return
                Defaults to all element types in assigned element types

        Return:
            dict:
                key: ElementType.element_type_id
                value: ElementValue object
        """
        result_dict = {}

        if not element_type_list:
            element_type_list = self.assigned_element_types

        for element_type in element_type_list:
            element_value_object = self.element_value(element_type)
            result_dict[element_type] = element_value_object

        return result_dict

    def __str__(self):
        name_element_type = ElementType.objects.get(entity_name="Name")
        name_value = self.get_element_value(name_element_type)
        return "{} - {}".format(self.datum_type, name_value)