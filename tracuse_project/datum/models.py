
from django.db import models

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

    # datum_types = relationship("DatumType", backref="datum_group")
    # group_rules = relationship("FilterRuleGroup", backref="datum_group")


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
                                    )

    # datum_objects = relationship("DatumObject", backref="datum_type")
    # element_types = relationship("ElementTypeDatumType", backref="datum_type")
    # type_rules = relationship("FilterRuleType", backref="datum_type")