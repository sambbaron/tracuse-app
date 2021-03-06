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
        all_associations (AssociationAll):
          All parent and child associations related to adjacent association
    """

    class Meta(AssociationModel.Meta):
        db_table = "association_adjacent"
        verbose_name = "Association Adjacent"
        verbose_name_plural = "Associations Adjacent"

    association_adjacent_id = models.AutoField(primary_key=True)
    parent_datum = models.ForeignKey("datum.DatumObject",
                                     db_column="parent_datum_id",
                                     related_name="adjacent_child_associations",
                                     null=False, blank=False
                                     )
    child_datum = models.ForeignKey("datum.DatumObject",
                                    db_column="child_datum_id",
                                    related_name="adjacent_parent_associations",
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

    @property
    def all_associations(self):
        """Get all associations related to adjacent association
        in AssociationAll
        """
        parent_datums_ids = AssociationAll.objects.filter(child_datum=self.child_datum).values_list("parent_datum_id", flat=True)
        child_datums_ids = AssociationAll.objects.filter(parent_datum=self.parent_datum).values_list("child_datum_id", flat=True)
        all_datum_ids = set(parent_datums_ids) & set(child_datums_ids)
        associations = AssociationAll.objects.filter(parent_datum_id__in=all_datum_ids, child_datum_id__in=all_datum_ids)
        return associations

    def _delete_associations(self):
        """Delete full path object associations from adjacent association
        Do not delete self associations
        """
        delete_associations = self.all_associations.exclude(distance=0)
        delete_associations.delete()

    def _set_associations(self):
        """Set full path object associations from adjacent association

        Update AssociationAll - create and delete

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
            new_assoc = AssociationAll.objects.update_or_create(
                defaults={"distance": parent_assoc.distance + 1},
                parent_datum=parent_assoc.parent_datum,
                child_datum=self.child_datum,
            )
            association_list.append(new_assoc[0])

        # Query related child associations for adjacent parent datum
        child_associations = AssociationAll.objects.filter(
            parent_datum=self.child_datum)

        # Create new child associations against adjacent parent datum
        for child_assoc in child_associations:
            new_assoc = AssociationAll.objects.update_or_create(
                defaults={"distance": child_assoc.distance + 1},
                parent_datum=self.parent_datum,
                child_datum=child_assoc.child_datum,
            )
            association_list.append(new_assoc[0])

        association_set = set(association_list)

        # Delete orphan associations not in list
        current_associations = set(self.all_associations)
        invalid_associations = current_associations - association_set
        for association in invalid_associations:
            association.delete()

        return association_set

    def save(self, *args, **kwargs):
        """Override save method

        Create associations in AssociationAll
        """
        super().save(*args, **kwargs)
        self._set_associations()

    def delete(self, using=None):
        """Override delete method

        Delete associations in AssociationAll
        """
        self._delete_associations()
        super().delete(using)


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
