from django.db import models

from django.contrib.auth.models import User

from common import mixins


class DatumGroup(mixins.DefinitionMixin):
    """Collection of Datum Types

    Has common functional uses

    Attributes:
        See DefinitionMixin (includes SortActiveMixin)
    """

    class Meta(mixins.DefinitionMixin.Meta):
        db_table = "datum_group"

    datum_group_id = models.AutoField(primary_key=True)


class DatumType(mixins.DefinitionMixin):
    """Type of Datum Objects

    Has common functional use and properties (elements)

    Attributes:
        See DefinitionMixin (includes SortActiveMixin)
        datum_group_id (integer, fk, required): DatumGroup
        repr_expression (string): Expression that results in
            representation string
    """

    class Meta(mixins.DefinitionMixin.Meta):
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


class DatumObject(mixins.SortActiveMixin):
    """Primary personal information data object

    Node/Vertex in graph
    Has Datum Type which defines properties (elements)

    Attributes:
        See SortActiveMixin
        user_id (integer, fk, required): User
        datum_type_id (integer, fk, required): DatumType
        creation_date (datetime)
    """

    class Meta(mixins.SortActiveMixin.Meta):
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
    creation_date = models.DateTimeField(auto_now_add=True)

    # TODO Property for associated Datums
    # TODO Property with element data