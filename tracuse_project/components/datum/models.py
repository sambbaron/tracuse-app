import re

from django.db import models

from django.contrib.auth.models import User

from utils.mixins import EntityMixin, BaseMixin
from components.element_type.models import ElementType, ElementTypeDatumObject
from components.association.models import AssociationAll


class DatumGroup(EntityMixin):
    """Collection of Datum Types

    Has common functional uses

    Attributes:
        See EntityMixin (includes BaseMixin)
            sort (integer): 2-digit number
    """

    class Meta(EntityMixin.Meta):
        db_table = "datum_group"
        verbose_name = "Datum Group"

    datum_group_id = models.AutoField(primary_key=True)

    sort_base_length = 2


class DatumType(EntityMixin):
    """Type of Datum Objects

    Has common functional use and properties (elements)

    Attributes:
        See EntityMixin (includes BaseMixin)
            sort (integer): DatumGroup.sort + 3-digit number
        datum_group_id (integer, fk, required): DatumGroup
        repr_expression (string): Expression that results in
            representation string referencing element types in {{}}
            --> {{name}} and {{description}}
        element_types (ElementType set):
            related element types from ElementTypeDatumType
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
    element_types = models.ManyToManyField("element_type.ElementType",
                                           through="element_type.ElementTypeDatumType",
                                           related_name="+"
                                           )
    sort_base_length = 3

    @property
    def sort_parts(self):
        return [self.datum_group.sort]


class DatumObject(BaseMixin):
    """Primary personal information data object

    Node/Vertex in graph
    Has Datum Type which defines properties (elements)

    Attributes:
        See BaseMixin
            sort (integer): DatumType.sort + single increment
        user_id (integer, fk, required): User
        datum_type_id (integer, fk, required): DatumType
        element_types (ElementType set):
            related element types from ElementTypeDatumObject
        datum_group (DatumGroup):
        default_element_types (list):
            ElementTypes from ElementTypeDatumType
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
    element_types = models.ManyToManyField("element_type.ElementType",
                                           through="element_type.ElementTypeDatumObject",
                                           related_name="+"
                                           )
    adjacent_child_datums = \
        models.ManyToManyField("self",
                               related_name="adjacent_parent_datums",
                               through="association.AssociationAdjacent",
                               symmetrical=False
                               )
    all_child_datums = \
        models.ManyToManyField("self",
                               related_name="all_parent_datums",
                               through="association.AssociationAll",
                               symmetrical=False
                               )

    sort_base_length = 1

    @property
    def sort_parts(self):
        return [self.datum_type.sort]


    def __str__(self):
        """Use DatumType.repr_expression with element type placeholders"""
        output = ""
        expression = self.datum_type.repr_expression
        if expression:
            for element_type in self.element_types_datum_objects.all():
                if element_type.element_value:
                    element_test = element_type.element_type.entity_name.lower()
                    expression = expression.replace("{{" + element_test + "}}",
                                                    element_type.get_element_value)

        # Remove placeholders not replaced
        expression = re.sub(r"\{\{.*?\}\}", "", expression)
        if expression:
            output = expression
        else:
            output = "Blank {}".format(self.datum_type)

        return output

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

    def element_value(self, element_type_object):
        """Retrieve Single Element Value Object for Element Type

        Arguments:
            element_type (ElementType object)

        Return:
            ElementValue object instance from model based on data type
        """

        if element_type_object not in self.element_types.all():
            return

        # Lookup ElementTypeDatumType object for association
        element_type_datum_object = self.element_types_datum_objects. \
            get(element_type=element_type_object)
        return element_type_datum_object.element_value

    def get_element_value(self, element_type_object):
        """Return value from ElementValue object
        Uses get_element_value property of ElementTypeDatumObject object

        Arguments:
            element_type (ElementType object)

        Return:
            ElementValue value: Data type depends on element type
        """
        if element_type_object not in self.element_types.all():
            return

        element_type_datum_object = self.element_types_datum_objects. \
            get(element_type=element_type_object)
        return element_type_datum_object.get_element_value

    def get_create_self_association(self):
        """Add datum association to itself if it doesn't exist

        Return:
            AssociationAll object
        """
        self_association = AssociationAll.get_create_association(
            parent_datum=self,
            child_datum=self,
            distance=0
        )
        return self_association

    def _get_adjacent_associated_datums(self, direction):
        """Return datums from AssociationAdjacent

        Arguments:
            direction (AssociationDirection):

        Returns:
            List of DatumObject objects
        """
        datums = []

        direction_name = direction.entity_name

        if direction_name is "parent" or direction_name is "both":
            parent_datums = self.adjacent_parent_datums.all()
            datums.extend(parent_datums)

        if direction_name is "child" or direction_name is "both":
            child_datums = self.adjacent_child_datums.all()
            datums.extend(child_datums)

        return datums

    def _get_all_associated_datums(self, direction, distance_limit=1):
        """Return associated datums from AssociationAll
        Does not include self

        Arguments:
            direction (AssociationDirection):
            distance_limit (integer):

        Returns:
            List of DatumObject objects
        """
        datums = []

        direction_name = direction.entity_name

        # Return parent datums where self is child
        if direction_name is "parent" or direction_name is "both":
            parent_datums = self.all_child_associations \
                .only("parent_datum") \
                .filter_distance(distance_limit) \
                .exclude_self(True) \
                .order_by("-distance") \
                .all()
            for datum in parent_datums:
                datums.append(datum.parent_datum)

        # Return child datums where self is parent
        if direction_name is "child" or direction_name is "both":
            child_datums = self.all_parent_associations \
                .only("child_datum") \
                .filter_distance(distance_limit) \
                .exclude_self(True) \
                .order_by("distance") \
                .all()
            for datum in child_datums:
                datums.append(datum.child_datum)

        return datums

    def get_associated_datums(self, direction, distance_limit=1):
        """Return associated datums depending on distance limit
        Use AssociationAdjacent if distance_limit = 1
        Use AssociationAll if distance_limit > 1

        Arguments:
            direction (AssociationDirection):
            distance_limit (integer, default=1):

        Returns:
            List of DatumObject objects
        """
        if distance_limit == 1:
            return self._get_adjacent_associated_datums(direction)
        else:
            return self._get_all_associated_datums(direction, distance_limit)

    def save(self, *args, **kwargs):
        """Override save method

        For new records:
            Create default element type assignment
                based on datum type

        For all records:
            Set self association if it doesn't exist
        """

        create_elements = False

        if self.pk is None:
            create_elements = True

        super().save(*args, **kwargs)

        # Create default elements
        if create_elements == True:
            for element_type in self.default_element_types:
                ElementTypeDatumObject.objects.create(datum_object=self,
                                                      element_type=element_type
                                                      )

        # Set self association
        self.get_create_self_association()

    ### UNUSED METHODS
    def element_values_dict(self, element_type_list=None):
        """Retrieve Multiple Element Values Objects for Datum Object

        Arguments:
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

    @property
    def as_dict_all(self):

        output_key = self.datum_object_id

        output = {
            output_key: {
                "group": self.datum_group.readable_name,
                "type": self.datum_type.readable_name,
                "headline": self.__str__()
            }
        }

        for element_type in self.assigned_element_types:
            element_value_key = element_type.readable_name
            element_value_value = self.get_element_value(element_type)
            output[output_key][element_value_key] = element_value_value

        # PLACEHOLDER FOR FORMATTING

        return output