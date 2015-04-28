from django.db import models

from django.contrib.auth.models import User

from common.mixins import EntityMixin, BaseMixin


class DatumGroup(EntityMixin):
    """Collection of Datum Types

    Has common functional uses

    Attributes:
        See EntityMixin (includes BaseMixin)
    """

    class Meta(EntityMixin.Meta):
        db_table = "datum_group"

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

    datum_type_id = models.AutoField(primary_key=True)

    datum_group = models.ForeignKey("DatumGroup",
                                    db_column="datum_group_id",
                                    related_name="datum_types",
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
        default_element_types (list):
            ElementTypes from ElementTypeDatumType
        assigned_element_types (list):
            ElementTypes from ElementTypeDatumObject

    Methods:
        element_values (dict):
            Return element_values for selected element_types

    """

    class Meta(BaseMixin.Meta):
        db_table = "datum_object"

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
    def default_element_types(self):
        element_types = []
        for datum_type_element_type in self.datum_type.element_types.all():
            element_types.append(datum_type_element_type.element_type)
        return element_types

    @property
    def assigned_element_types(self):
        element_types = []
        for datum_object_element_type in self.element_types.all():
            element_types.append(datum_object_element_type.element_type)
        return element_types

    def element_values(self, element_type_list=None):
        """Retrieve Element Values for Datum Object

        Args:
            element_type_list (list):
                List of ElementType objects
                Defaults to assigned element types

        Return:
            dict:
                key: ElementType object
                value: ElementValue object
        """
        result_dict = {}

        if not element_type_list:
            element_type_list = self.assigned_element_types

        # Loop through element types
        for element_type in element_type_list:
            element_type_id = element_type.element_type_id
            # Lookup ElementTypeDatumType object for association
            element_type_datum_object = self.element_types.get(element_type=element_type)
            # Lookup ElementValueModel value
            element_value = element_type_datum_object.element_value_object
            result_dict[element_type] = element_value

        return result_dict
