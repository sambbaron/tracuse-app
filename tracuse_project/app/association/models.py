from django.db import models

from app.common.models import EntityModel, BaseModel

from .managers import AssociationManager


class AssociationType(EntityModel):
    """Types of relationships/edges between Datums

    Attributes:
        See EntityModel (includes BaseModel)
    """

    class Meta(EntityModel.Meta):
        db_table = "association_type"
        verbose_name = "Association Type"

    association_type_id = models.AutoField(primary_key=True)

    sort_base_length = 3


class AssociationDirection(EntityModel):
    """Direction of Association from a particular Datum (node)

    Used for filters

    Examples:
        Parent (Backwards), Child (Forwards), Both

    Attributes:
        See EntityModel (includes BaseModel)
    """

    class Meta(EntityModel.Meta):
        db_table = "association_direction"
        verbose_name = "Association Direction"

    association_direction_id = models.IntegerField(primary_key=True)

    sort_base_length = 3

    @classmethod
    def parent(cls):
        return cls.objects.get(pk=-1)

    @classmethod
    def both(cls):
        return cls.objects.get(pk=0)

    @classmethod
    def child(cls):
        return cls.objects.get(pk=1)


class AssociationModel(BaseModel):
    """Common columns for Association models

    Attributes:
        See BaseModel
        parent_datum_id (integer, pk, fk): DatumObject
        child_datum_id (integer, pk, fk): DatumObject
    """

    class Meta(BaseModel.Meta):
        abstract = True
        unique_together = ("parent_datum", "child_datum")
        index_together = ("parent_datum", "child_datum")

        # parent_datum and child_datum in child classes
        # distinction is related name


class AssociationAdjacent(AssociationModel):
    """Direct relationships between Datums

    Edge/Link in graph

    Attributes:
        See AssociationModel (includes BaseModel)
        association_type_id (integer, fk, required): AssociationType
    """

    class Meta(AssociationModel.Meta):
        db_table = "association_adjacent"
        verbose_name = "Association Adjacent"
        verbose_name_plural = "Associations Adjacent"

    association_adjacent_id = models.AutoField(primary_key=True)
    parent_datum = models.ForeignKey("datum.DatumObject",
                                     db_column="parent_datum_id",
                                     related_name="adjacent_parent_associations",
                                     null=False, blank=False
                                     )
    child_datum = models.ForeignKey("datum.DatumObject",
                                    db_column="child_datum_id",
                                    related_name="adjacent_child_associations",
                                    null=False, blank=False
                                    )
    association_type = models.ForeignKey("AssociationType",
                                         db_column="association_type_id",
                                         related_name="associations_adjacent",
                                         null=False, blank=False
                                         )


    def __str__(self):
        return "{} -> {} = {}".format(
            self.parent_datum.__str__(),
            self.child_datum.__str__(),
            self.association_type.readable_name
        )

    def get_all_associations(self):
        """Get all associations in AssociationAll"""
        parent_expr = models.Q(parent_datum=self.parent_datum) | models.Q(parent_datum=self.child_datum)
        child_expr = models.Q(child_datum=self.child_datum) | models.Q(child_datum=self.parent_datum)
        filter_expr = parent_expr | child_expr
        associations = AssociationAll.objects.filter(filter_expr).all()
        return associations

    def _delete_associations(self):
        """Delete full path object associations from adjacent association"""

    def _create_associations(self):
        """Create full path object associations from adjacent association

        Returns:
            Association Set
        """

        association_list = []

        # Set self-referential association for both parent and child datum
        parent_self_association = self.parent_datum.get_create_self_association()
        child_self_association = self.child_datum.get_create_self_association()
        association_list.extend([parent_self_association, child_self_association])

        # Query related parent associations for adjacent child datum
        parent_associations = AssociationAll.objects.filter(
            child_datum=self.parent_datum)

        # Create new parent associations against adjacent child datum
        for parent_assoc in parent_associations:
            new_assoc = AssociationAll.objects.get_or_create(
                parent_datum=parent_assoc.parent_datum,
                child_datum=self.child_datum,
                distance=parent_assoc.distance + 1
            )
            association_list.append(new_assoc[0])

        # Query related child associations for adjacent parent datum
        child_associations = AssociationAll.objects.filter(
            parent_datum=self.child_datum)

        # Create new child associations against adjacent parent datum
        for child_assoc in child_associations:
            new_assoc = AssociationAll.objects.get_or_create(
                parent_datum=self.parent_datum,
                child_datum=child_assoc.child_datum,
                distance=child_assoc.distance + 1
            )
            association_list.append(new_assoc[0])

        return set(association_list)

    def set_associations(self):
        """Delete existing and create full path object associations
        for given adjacent association"""
        self._create_associations()

    def save(self, *args, **kwargs):
        """Override save method

        For all records:
            Set association in AssociationAll
        """
        super().save(*args, **kwargs)

        # Set association
        self.set_associations()


class AssociationAll(AssociationModel):
    """All relationships between Datums

    Closure table pattern
    Stores every path through tree

    Attributes:
        See AssociationModel (includes BaseModel)
        distance (integer, default=0):
            number of steps between association
    """

    class Meta(AssociationModel.Meta):
        db_table = "association_all"
        verbose_name = "Association All"
        verbose_name_plural = "Associations All"

    association_all_id = models.AutoField(primary_key=True)
    parent_datum = models.ForeignKey("datum.DatumObject",
                                     db_column="parent_datum_id",
                                     related_name="all_child_associations",
                                     null=False, blank=False
                                     )
    child_datum = models.ForeignKey("datum.DatumObject",
                                    db_column="child_datum_id",
                                    related_name="all_parent_associations",
                                    null=False, blank=False
                                    )
    distance = models.IntegerField(default=0)


    def __str__(self):
        return "{} -> {} = {}".format(
            self.parent_datum.__str__(),
            self.child_datum.__str__(),
            self.distance
        )

    # Custom queryset methods for
    # filter_distance and exclude_self
    objects = AssociationManager()

    @staticmethod
    def get_create_association(parent_datum, child_datum, distance):
        """Add association if it doesn't exist

        Uses Django get_or_create queryset method

        Return:
            AssociationAll object
        """
        association = AssociationAll.objects.get_or_create(
            parent_datum=parent_datum,
            child_datum=child_datum,
            distance=distance
        )
        return association[0]