from django.db import models

from utils.mixins import EntityMixin, BaseMixin


class AssociationType(EntityMixin):
    """Types of relationships/edges between Datums

    Attributes:
        See EntityMixin (includes BaseMixin)
    """

    class Meta(EntityMixin.Meta):
        db_table = "association_type"
        verbose_name = "Association Type"

    association_type_id = models.AutoField(primary_key=True)


class AssociationDirection(EntityMixin):
    """Direction of Association from a particular Datum (node)

    Used for filters

    Examples:
        Parent (Backwards), Child (Forwards), Both

    Attributes:
        See EntityMixin (includes BaseMixin)
    """

    class Meta(EntityMixin.Meta):
        db_table = "association_direction"
        verbose_name = "Association Direction"

    association_direction_id = models.AutoField(primary_key=True)


class AssociationMixin(BaseMixin):
    """Common columns for Association models

    Attributes:
        See BaseMixin
        parent_datum_id (integer, pk, fk): DatumObject
        child_datum_id (integer, pk, fk): DatumObject
    """

    class Meta(BaseMixin.Meta):
        abstract = True
        unique_together = ("parent_datum", "child_datum")
        index_together = ("parent_datum", "child_datum")

    # FIXME Django Limitation - composite primary keys
    parent_datum = models.ForeignKey("datum.DatumObject",
                                     db_column="parent_datum_id",
                                     related_name="+",
                                     null=False, blank=False
                                     )
    child_datum = models.ForeignKey("datum.DatumObject",
                                    db_column="child_datum_id",
                                    related_name="+",
                                    null=False, blank=False
                                    )

    def __str__(self):
        return "{} -> {}".format(
            self.parent_datum.__str__(),
            self.child_datum.__str__()
        )


class AssociationAdjacent(AssociationMixin):
    """Direct relationships between Datums

    Edge/Link in graph

    Attributes:
        See AssociationMixin (includes BaseMixin)
        association_type_id (integer, fk, required): AssociationType
    """

    class Meta(AssociationMixin.Meta):
        db_table = "association_adjacent"
        verbose_name = "Association Adjacent"
        verbose_name_plural = "Associations Adjacent"

    association_adjacent_id = models.AutoField(primary_key=True)
    association_type = models.ForeignKey("AssociationType",
                                         db_column="association_type_id",
                                         related_name="associations_adjacent",
                                         null=False, blank=False
                                         )


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
                child_datum=self.child_datum
            )
            association_list.append(new_assoc[0])

        # Query related child associations for adjacent parent datum
        child_associations = AssociationAll.objects.filter(
            parent_datum=self.child_datum)

        # Create new child associations against adjacent parent datum
        for child_assoc in child_associations:
            new_assoc = AssociationAll.objects.get_or_create(
                parent_datum=self.parent_datum,
                child_datum=child_assoc.child_datum
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



class AssociationAll(AssociationMixin):
    """All relationships between Datums

    Closure table pattern
    Stores every path through tree

    Attributes:
        See AssociationMixin (includes BaseMixin)
        depth (integer, default=0):
            only used in searches
    """

    class Meta(AssociationMixin.Meta):
        db_table = "association_all"
        verbose_name = "Association All"
        verbose_name_plural = "Associations All"

    association_all_id = models.AutoField(primary_key=True)
    depth = models.IntegerField(default=0)

    @staticmethod
    def get_create_association(parent_datum, child_datum):
        """Add association if it doesn't exist

        Uses Django get_or_create queryset method

        Return:
            AssociationAll object
        """
        association = AssociationAll.objects.get_or_create(
            parent_datum=parent_datum,
            child_datum=child_datum,
        )
        return association[0]