from django.db import models

from django.contrib.auth.models import User

from app.common.models import EntityModel, BaseModel


class FilterRuleModel(BaseModel):
    """Common properties for Filter Rules

    Attributes:
        See BaseModel
        operator (string, required):
            Converted to Django field lookup expression
        conditional (string, optional): And, Or
    """

    class Meta(BaseModel.Meta):
        abstract = True

    OPERATOR_CHOICES = (
        ("iexact", "equals"),

        ("Text", (
            ("contains", "contains"),
            ("istartswith", "starts with"),
            ("iendswith", "ends with"),
        )
         ),

        ("Number", (
            ("gt", "greater than"),
            ("gte", "greater than or equal to"),
            ("lt", "less than"),
            ("lte", "less than or equal to"),
        )
         ),

        ("Datetime", (
            ("year", "year"),
            ("month", "month"),
            ("day", "day"),
            ("week_day", "weekday"),
            ("hour", "hour"),
            ("minute", "minute"),
        )
         )
    )

    CONDITIONAL_CHOICES = (
        ("and", "and"),
        ("or", "or"),
    )

    operator = models.CharField(max_length=5,
                                default="iexact",
                                null=False, blank=False,
                                choices=OPERATOR_CHOICES
                                )
    conditional = models.CharField(max_length=3,
                                   null=True, blank=True,
                                   choices=CONDITIONAL_CHOICES
                                   )


class FilterRuleGroup(FilterRuleModel):
    """Filter Rules by Datum Group

    Attributes:
        See FilterRuleModel (includes BaseModel)
        datum_group_id (integer, fk, required): DatumGroup
    """

    class Meta(FilterRuleModel.Meta):
        db_table = "filter_rule_group"
        verbose_name = "Filter Rule - Group"

    filter_rule_group_id = models.AutoField(primary_key=True)
    datum_group = models.ForeignKey("datum.DatumGroup",
                                    db_column="datum_group_id",
                                    related_name="filter_rule_groups",
                                    null=False, blank=False
                                    )


class FilterRuleType(FilterRuleModel):
    """Filter Rules by Datum Type

    Attributes:
        See FilterRuleModel (includes BaseModel)
        datum_type_id (integer, fk, required): DatumType
    """

    class Meta(FilterRuleModel.Meta):
        db_table = "filter_rule_type"
        verbose_name = "Filter Rule - Type"

    filter_rule_type_id = models.AutoField(primary_key=True)
    datum_type = models.ForeignKey("datum.DatumType",
                                   db_column="datum_type_id",
                                   related_name="filter_rule_types",
                                   null=False, blank=False
                                   )


class FilterRuleAssociation(FilterRuleModel):
    """Filter Rules by Datum Association

    Attributes:
        See FilterRuleModel (includes BaseModel)
        datum_object_id (integer, fk, required): DatumObject
        association_direction_id (integer, fk, required): AssociationDirection
        association_type_id (integer, fk, required): AssociationType
        distance (integer, required): from datum object
    """

    class Meta(FilterRuleModel.Meta):
        db_table = "filter_rule_association"
        verbose_name = "Filter Rule - Association"

    filter_rule_association_id = models.AutoField(primary_key=True)
    datum_object = models.ForeignKey("datum.DatumObject",
                                     db_column="datum_object_id",
                                     related_name="filter_rule_associations",
                                     null=False, blank=False
                                     )
    association_direction = models.ForeignKey("association.AssociationDirection",
                                              db_column="association_direction_id",
                                              related_name="filter_rule_associations",
                                              null=False, blank=False
                                              )
    association_type_id = models.ForeignKey("association.AssociationType",
                                            db_column="association_type_id",
                                            related_name="filter_rule_associations",
                                            null=False, blank=False
                                            )
    distance = models.IntegerField(default=1,
                                   null=False, blank=False
                                   )


class FilterRuleElement(FilterRuleModel):
    """Filter Rules by Element Value

    Attributes:
        See FilterRuleModel (includes BaseModel)
        element_type_id (integer, fk, required): ElementType
        elvalue (string):  ***Must match value
    """

    class Meta(FilterRuleModel.Meta):
        db_table = "filter_rule_element"
        verbose_name = "Filter Rule - Element"

    filter_rule_element_id = models.AutoField(primary_key=True)
    element_type = models.ForeignKey("element_type.ElementType",
                                     db_column="element_type_id",
                                     related_name="filter_rule_elements",
                                     null=False, blank=False
                                     )
    elvalue = models.CharField(max_length=255)


class FilterSet(EntityModel):
    """Datum Filters with rules

    Multiple Uses: Views and Associations

    Attributes:
        See EntityModel (includes BaseModel)
        user_id (integer, fk, optional): User
    """

    class Meta(EntityModel.Meta):
        db_table = "filter_set"
        verbose_name = "Filter Set"

    filter_set_id = models.AutoField(primary_key=True)
    # Null user means filter set available to all users??
    user_id = models.ForeignKey(User,
                                db_column="user_id",
                                related_name="filter_sets",
                                null=True, blank=True
                                )


class FilterSetRuleModel(BaseModel):
    """Common properties for assigning Filter Rules to Filter Sets

    Includes rule ordering

    Attributes:
        See BaseModel
        filter_set_id (integer, fk, required): FilterSet
    """

    class Meta(BaseModel.Meta):
        abstract = True

    filter_set_id = models.ForeignKey("FilterSet",
                                      db_column="filter_set_id",
                                      null=False, blank=False
                                      )


class FilterSetGroupRule(FilterSetRuleModel):
    """Assign Group Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleModel (includes Base)
        filter_rule_group_id (integer, fk, required): FilterRuleGroup
    """

    class Meta(BaseModel.Meta):
        db_table = "filter_set_group_rule"
        default_related_name = "filter_set_group_rules"

    filter_set_group_rule_id = models.AutoField(primary_key=True)
    filter_rule_group_id = models.ForeignKey("FilterRuleGroup",
                                             db_column="filter_rule_group_id",
                                             null=False, blank=False
                                             )


class FilterSetTypeRule(FilterSetRuleModel):
    """Assign Type Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleModel (includes Base)
        filter_rule_type_id (integer, fk, required): FilterRuleType
    """

    class Meta(BaseModel.Meta):
        db_table = "filter_set_type_rule"
        default_related_name = "filter_set_type_rules"

    filter_set_type_rule_id = models.AutoField(primary_key=True)
    filter_rule_type_id = models.ForeignKey("FilterRuleType",
                                            db_column="filter_rule_type_id",
                                            null=False, blank=False
                                            )


class FilterSetAssociationRule(FilterSetRuleModel):
    """Assign Association Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleModel (includes Base)
        filter_rule_association_id (integer, fk, required): FilterRuleAssociation
    """

    class Meta(BaseModel.Meta):
        db_table = "filter_set_association_rule"
        default_related_name = "filter_set_association_rules"

    filter_set_association_rule_id = models.AutoField(primary_key=True)
    filter_rule_association_id = models.ForeignKey("FilterRuleAssociation",
                                                   db_column="filter_rule_association_id",
                                                   null=False, blank=False
                                                   )


class FilterSetElementRule(FilterSetRuleModel):
    """Assign Element Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleModel (includes Base)
        filter_rule_element_id (integer, fk, required): FilterRuleElement
    """

    class Meta(BaseModel.Meta):
        db_table = "filter_set_element_rule"
        default_related_name = "filter_set_element_rules"

    filter_set_element_rule_id = models.AutoField(primary_key=True)
    filter_rule_element_id = models.ForeignKey("FilterRuleElement",
                                               db_column="filter_rule_element_id",
                                               null=False, blank=False
                                               )
