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
                                    null=False, blank=False,
                                    db_index=True
                                    )
    repr_expression = models.CharField(max_length=255,
                                       null=False, blank=False
                                       )


class DatumObject(BaseMixin):
    """Primary personal information data object

    Node/Vertex in graph
    Has Datum Type which defines properties (elements)

    Attributes:
        See BaseMixin
        user_id (integer, fk, required): User
        datum_type_id (integer, fk, required): DatumType
        creation_date (datetime)
    """

    class Meta(BaseMixin.Meta):
        db_table = "datum_object"

    datum_object_id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User,
                             db_column="user_id",
                             null=False, blank=False,
                             db_index=True
                             )
    datum_type = models.ForeignKey("DatumType",
                                   db_column="datum_type_id",
                                   null=False, blank=False,
                                   db_index=True
                                   )


    # TODO Property for associated Datums
    # TODO Property with element data