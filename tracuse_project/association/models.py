from django.db import models

from common.mixins import EntityMixin, BaseMixin


class AssociationType(EntityMixin):
    """Types of relationships/edges between Datums

    Attributes:
        See EntityMixin (includes BaseMixin)
    """

    class Meta(EntityMixin.Meta):
        db_table = "association_type"

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


class AssociationAdjacent(AssociationMixin):
    """Direct relationships between Datums

    Edge/Link in graph

    Attributes:
        See AssociationMixin (includes BaseMixin)
        association_type_id (integer, fk, required): AssociationType
    """

    class Meta(AssociationMixin.Meta):
        db_table = "association_adjacent"

    association_adjacent_id = models.AutoField(primary_key=True)
    association_type = models.ForeignKey("AssociationType",
                                         db_column="association_type_id",
                                         related_name="associations_adjacent",
                                         null=False, blank=False
                                         )


class AssociationAll(AssociationMixin):
    """All relationships between Datums

    Closure table pattern
    Stores every path through tree

    Attributes:
        See AssociationMixin (includes BaseMixin)
        depth (integer):
    """

    class Meta(AssociationMixin.Meta):
        db_table = "association_all"

    association_all_id = models.AutoField(primary_key=True)
    depth = models.IntegerField(default=0)


class AssociationKeyword(BaseMixin):
    """Keywords in Datum that trigger dynamic association

    Attributes:
        See BaseMixin
        datum_object_id (integer, fk, required):
            DatumObject to be associated
        keyword (string, required)
        filter_test_scope (integer, fk, optional):
            FilterSet used to limit scope of keyword test
            If null, then keyword is tested against all objects
    """

    class Meta(BaseMixin.Meta):
        db_table = "association_keyword"

    association_keyword_id = models.AutoField(primary_key=True)
    datum_object = models.ForeignKey("datum.DatumObject",
                                     db_column="datum_object_id",
                                     related_name="association_keywords",
                                     null=False, blank=False
                                     )
    keyword = models.CharField(max_length=100,
                               null=False, blank=False
                               )
    # filter_test_scope = models.ForeignKey("filter.FilterSet",
    # db_column="filter_set_id",
    # related_name="association_keywords",
    # null=True, blank=True
    #                                       )