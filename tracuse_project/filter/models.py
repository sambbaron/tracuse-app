from django.db import models

from django.contrib.auth.models import User

from common.mixins import EntityMixin, BaseMixin


class FilterRuleMixin(BaseMixin):
    """Common properties for Filter Rules

    Attributes:
        See BaseMixin
        operator (string, required):  -> = <> => <=
        conditional (string, nullable): And, Or
    """

    class Meta(BaseMixin.Meta):
        abstract = True
        db_table = ""
        default_related_name = db_table + "s"

    CONDITIONAL_CHOICES = (
        ('AND', 'AND'),
        ('OR', 'OR'),
    )

    operator = models.CharField(max_length=5,
                                default="=",
                                null=False, blank=False
                                )
    conditional = models.CharField(max_length=3,
                                   null=True, blank=True,
                                   choices=CONDITIONAL_CHOICES
                                   )


class FilterRuleGroup(FilterRuleMixin):
    """Filter Rules by Datum Group

    Attributes:
        See FilterRuleMixin (includes BaseMixin)
        datum_group_id (integer, fk, required): DatumGroup
    """

    class Meta(FilterRuleMixin.Meta):
        db_table = "filter_rule_group"

    filter_rule_group_id = models.AutoField(primary_key=True)
    datum_group = models.ForeignKey("datum.DatumGroup",
                                    db_column="datum_group_id",
                                    null=False, blank=False
                                    )


class FilterRuleType(FilterRuleMixin):
    """Filter Rules by Datum Type

    Attributes:
        See FilterRuleMixin (includes BaseMixin)
        datum_type_id (integer, fk, required): DatumType
    """

    class Meta(FilterRuleMixin.Meta):
        db_table = "filter_rule_type"

    filter_rule_type_id = models.AutoField(primary_key=True)
    datum_type = models.ForeignKey("datum.DatumType",
                                   db_column="datum_type_id",
                                   null=False, blank=False
                                   )


class FilterRuleAssociation(FilterRuleMixin):
    """Filter Rules by Datum Association

    Attributes:
        See FilterRuleMixin (includes BaseMixin)
        datum_object_id (integer, fk, required): DatumObject
        association_direction_id (integer, fk, required): AssociationDirection
        association_type_id (integer, fk, required): AssociationType
        depth (integer, required)
    """

    class Meta(FilterRuleMixin.Meta):
        db_table = "filter_rule_association"

    filter_rule_association_id = models.AutoField(primary_key=True)
    datum_object = models.ForeignKey("datum.DatumObject",
                                     db_column="datum_object_id",
                                     null=False, blank=False
                                     )
    association_direction = models.ForeignKey("association.AssociationDirection",
                                              db_column="association_direction_id",
                                              null=False, blank=False
                                              )
    association_type_id = models.ForeignKey("association.AssociationType",
                                            db_column="association_type_id",
                                            null=False, blank=False
                                            )
    depth = models.IntegerField(default=1,
                                null=False, blank=False
                                )


class FilterRuleElement(FilterRuleMixin):
    """Filter Rules by Element Value

    Attributes:
        See FilterRuleMixin (includes BaseMixin)
        element_type_id (integer, fk, required): ElementType
        element_value (string):  ***Must match value
    """


    class Meta(FilterRuleMixin.Meta):
        db_table = "filter_rule_element"

    filter_rule_element_id = models.AutoField(primary_key=True)
    element_type = models.ForeignKey("element_type.ElementType",
                                     db_column="element_type_id",
                                     null=False, blank=False
                                     )
    element_value = models.CharField(max_length=255)


class FilterSet(EntityMixin):
    """Datum Filters with rules

    Multiple Uses: Views and Associations

    Attributes:
        See EntityMixin (includes BaseMixin)
        user_id (integer, fk, nullable): User
    """

    class Meta(EntityMixin.Meta):
        db_table = "filter_set"

    filter_set_id = models.AutoField(primary_key=True)
    # Null user means filter set available to all users??
    user_id = models.ForeignKey(User,
                                db_column="user_id",
                                null=True, blank=True
                                )


class FilterSetRuleMixin(BaseMixin):
    """Common properties for assigning Filter Rules to Filter Sets

    Includes rule ordering

    Attributes:
        See BaseMixin
        filter_set_id (integer, fk, required): FilterSet
    """

    class Meta(BaseMixin.Meta):
        abstract = True
        db_table = ""
        default_related_name = db_table + "s"

    filter_set_id = models.ForeignKey("FilterSet",
                                      db_column="filter_set_id",
                                      null=False, blank=False
                                      )


class FilterSetGroupRule(FilterSetRuleMixin):
    """Assign Group Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleMixin (includes Base)
        filter_rule_group_id (integer, fk, required): FilterRuleGroup
    """

    class Meta(BaseMixin.Meta):
        db_table = "filter_set_group_rule"

    filter_set_group_rule_id = models.AutoField(primary_key=True)
    filter_rule_group_id = models.ForeignKey("FilterRuleGroup",
                                             "filter_rule_group_id",
                                             null=False, blank=False
                                             )


class FilterSetTypeRule(FilterSetRuleMixin):
    """Assign Type Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleMixin (includes Base)
        filter_rule_type_id (integer, fk, required): FilterRuleType
    """

    class Meta(BaseMixin.Meta):
        db_table = "filter_set_type_rule"

    filter_set_type_rule_id = models.AutoField(primary_key=True)
    filter_rule_type_id = models.ForeignKey("FilterRuleType",
                                            "filter_rule_type_id",
                                            null=False, blank=False
                                            )


class FilterSetAssociationRule(FilterSetRuleMixin):
    """Assign Association Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleMixin (includes Base)
        filter_rule_association_id (integer, fk, required): FilterRuleAssociation
    """

    class Meta(BaseMixin.Meta):
        db_table = "filter_set_association_rule"

    filter_set_association_rule_id = models.AutoField(primary_key=True)
    filter_rule_association_id = models.ForeignKey("FilterRuleAssociation",
                                                   "filter_rule_association_id",
                                                   null=False, blank=False
                                                   )


class FilterSetElementRule(FilterSetRuleMixin):
    """Assign Element Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleMixin (includes Base)
        filter_rule_element_id (integer, fk, required): FilterRuleElement
    """

    class Meta(BaseMixin.Meta):
        db_table = "filter_set_element_rule"

    filter_set_element_rule_id = models.AutoField(primary_key=True)
    filter_rule_element_id = models.ForeignKey("FilterRuleElement",
                                               "filter_rule_element_id",
                                               null=False, blank=False
                                               )