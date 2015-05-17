from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.template import Context, Template

from django.contrib.auth.models import User

from app.common.models import EntityModel, BaseModel
from app.element_type.models import ElementType, ElementDatumObject
from app.element_value.models import ElementValueMeta
from app.association.models import AssociationAll

from .datum_methods import DatumObjectMethodFactory
from app.common.serializers import Serializer


class DatumGroup(EntityModel):
    """Collection of Datum Types

    Has common functional uses

    Attributes:
        See EntityModel (includes BaseModel)
            sort (integer): 2-digit number
    """

    class Meta(EntityModel.Meta):
        db_table = "datum_group"
        verbose_name = "Datum Group"

    datum_group_id = models.AutoField(primary_key=True)

    sort_base_length = 2


class DatumType(EntityModel):
    """Type of Datum Objects

    Has common functional use and properties (elements)

    Attributes:
        See EntityModel (includes BaseModel)
            sort (integer): DatumGroup.sort + 3-digit number
        datum_group_id (integer, fk, required): DatumGroup
        headline_expr (string): Expression in django template language
            that renders to string representation
            --> {{name}} and {{description}}
        element_types (ElementType set):
            related element types from ElementDatumType
    """

    class Meta(EntityModel.Meta):
        db_table = "datum_type"
        verbose_name = "Datum Type"

    datum_type_id = models.AutoField(primary_key=True)

    datum_group = models.ForeignKey("DatumGroup",
                                    db_column="datum_group_id",
                                    null=False, blank=False,
                                    db_index=True
                                    )
    headline_expr = models.CharField(max_length=255,
                                      null=False, blank=False
                                      )
    element_types = models.ManyToManyField("element_type.ElementType",
                                           through="element_type.ElementDatumType",
                                           related_name="+"
                                           )
    sort_base_length = 3

    @property
    def sort_parts(self):
        return [self.datum_group.sort]


class DatumObject(BaseModel):
    """Primary personal information data object

    Node/Vertex in graph
    Has Datum Type which defines properties (elements)

    Attributes:
        See BaseModel
            sort (integer): DatumType.sort + single increment
        user_id (integer, fk, required): User
        datum_type_id (integer, fk, required): DatumType
        element_types (ElementType set):
            related element types from ElementDatumObject
        datum_group (DatumGroup):
        default_element_types (list):
            ElementTypes from ElementDatumType
            Return element values for multiple element types
        elements (queryset):
            ElementDatumObject objects
    """

    class Meta(BaseModel.Meta):
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
                                           through="element_type.ElementDatumObject",
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

    def __init__(self, *args, **kwargs):
        """Set method class for DatumType-specific methods"""
        super().__init__(*args, **kwargs)
        self.datum_methods = DatumObjectMethodFactory(
            datum_object=self,
            datum_type_name=self.datum_type.entity_name
        )

    @property
    def sort_parts(self):
        return [self.datum_type.sort]

    @property
    def headline(self):
        """Use DatumType.headline_expr with django template expression"""
        output = ""
        expression = self.datum_type.headline_expr

        if expression:
            template = Template(expression)
            element_dict = Serializer(data=self,
                                      serializer="datum.DatumObjectSerializer.serial_element_name_value"
                                      ).serialize()
            context = Context(element_dict)
            output = template.render(context)

        if not output or output is None:
            output = "Blank {}".format(self.datum_type)

        return output


    def __str__(self):
        return self.headline

    @property
    def datum_group(self):
        return self.datum_type.datum_group

    @property
    def default_element_types(self):
        element_types = []
        for datum_type_element_type in self.datum_type.element_datum_types.all():
            related_element_type = datum_type_element_type.element_type
            element_types.append(related_element_type)
        return element_types

    @property
    def elements(self):
        return self.element_datum_objects.all()


    def element_value(self, element_type_object=None, **kwargs):
        """Return element_value object for given element_type object

        Arguments:
            element_type_object (ElementType)
            **kwargs: element type filter to lookup element type

        Returns:
            ElementValue(Model) object
        """
        if not element_type_object:
            element_type_object = ElementType.objects.filter(**kwargs).first()

        if element_type_object:
            try:
                element_datum_object = self.elements.get(element_type=element_type_object)
                return element_datum_object.element_value
            except ObjectDoesNotExist as e:
                print("{} does not have element {}".format(
                    self.__str__(),
                    element_type_object.__str__()
                ))

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

    def get_associations(self, direction, distance_limit=1):
        """Return associations from AssociationAll
        Excludes self association

        Arguments:
            direction (AssociationDirection):
            distance_limit (integer):

        Returns:
            List of AssociationAll objects
        """
        associations = []

        # Return parent associations where self is child
        if direction.entity_name is "parent" or direction.entity_name is "both":
            query = self.all_child_associations
            query = query.filter_distance(distance_limit)
            query = query.exclude_self(True)
            query = query.order_by("-distance")
            parent_associations = query.all()
            associations.extend(parent_associations)

        # Return child associations where self is parent
        if direction.entity_name is "child" or direction.entity_name is "both":
            query = self.all_parent_associations
            query = query.filter_distance(distance_limit)
            query = query.exclude_self(True)
            query = query.order_by("distance")
            child_associations = query.all()
            associations.extend(child_associations)

        return associations

    def get_associated_datums(self, direction, distance_limit=1):
        """Return associated datums from AssociationAll
        Includes self

        Arguments:
            direction (AssociationDirection):
            distance_limit (integer):

        Returns:
            List of DatumObject objects
        """
        datums = []

        associations = self.get_associations(
            direction=direction,
            distance_limit=distance_limit
        )

        for association in associations:
            if direction.entity_name is "parent" or direction.entity_name is "both" \
                    and association.parent_datum is not self:
                datums.append(association.parent_datum)
            if direction.entity_name is "child" or direction.entity_name is "both" \
                    and association.child_datum is not self:
                datums.append(association.child_datum)

        # 'Both' direction causes self append twice
        # 'Parent' and 'Child' direction does not append self
        # So append self manually
        datums.append(self)

        return datums

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
                # Create ElementDatumObject object
                element_datum_object = \
                    ElementDatumObject. \
                        objects.create(datum_object=self,
                                       element_type=element_type
                                       )

                # Create ElementValue object
                data_type_name = element_type.element_data_type.entity_name
                ElementValueMeta(data_type_name=data_type_name). \
                    objects.create(element_datum_object=
                                   element_datum_object)

        # Set self association
        self.get_create_self_association()