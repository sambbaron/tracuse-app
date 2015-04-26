
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
        datum_group_id: (integer, fk, required): DatumGroup
    """

    class Meta(mixins.DefinitionMixin.Meta):
        db_table = "datum_type"

    datum_type_id = models.AutoField(primary_key=True)

    datum_group = models.ForeignKey("DatumGroup",
                                    db_column="datum_group_id",
                                    null=False,
                                    db_index=True,
                                    blank=False
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
                             null=False,
                             db_index=True,
                             blank=False
                             )
    datum_type = models.ForeignKey("DatumType",
                                   db_column="datum_type_id",
                                   null=False,
                                   db_index=True,
                                   blank=False
                                   )
    creation_date = models.DateTimeField(auto_now_add=True,
                                         db_default="CURRENT_TIMESTAMP"
                                         )

    #TODO Property for associated Datums
    #TODO Property with element data