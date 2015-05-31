from itertools import chain

from django.db import models

from django.contrib.auth.models import User

from app.common.models import EntityModel, BaseModel
from app.association.models import AssociationDirection
from app.element_value.models import ElementValueMeta

from .utils import compile_Q_objects, run_filter_from_model


class FilterRuleModel(BaseModel):
    """Common properties for Filter Rules

    Attributes:
        See BaseModel
        operator (string, required):
            Converted to Django field lookup expression
        conditional (string, optional, default="AND"):
            Applied before filter rule
            First rule does not need conditional
    """

    class Meta(BaseModel.Meta):
        abstract = True

    OPERATOR_CHOICES = (
        ("exact", "equals"),

        ("Text", (
            ("iexact", "text equals"),
            ("icontains", "contains"),
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
        ("AND", "AND"),
        ("OR", "OR"),
    )

    operator = models.CharField(max_length=25,
                                default="exact",
                                null=False, blank=False,
                                choices=OPERATOR_CHOICES
                                )
    conditional = models.CharField(max_length=3,
                                   null=True, blank=True,
                                   default="AND",
                                   choices=CONDITIONAL_CHOICES
                                   )


class FilterRuleQModel(FilterRuleModel):
    """Filter rule that outputs Q object

    Used for datum property filters

    Attributes:
        See FilterRuleModel (includes BaseModel)
        lookup_field (string):
        lookup_value (variable)
    """

    class Meta(FilterRuleModel.Meta):
        abstract = True

    @property
    def lookup_field(self):
        pass

    @property
    def lookup_value(self):
        pass

    def Q_object(self, lookup_prefix):
        """Return queryset Q object with lookup expression

        Arguments:
            lookup_prefix (string):
                field path to datum object

        Returns:
            Q object
        """

        lookup = self.lookup_field
        if lookup_prefix:
            lookup = lookup_prefix + "__" + self.lookup_field

        lookup_expression = lookup + "__" + self.operator
        query_object = (lookup_expression, self.lookup_value)
        return models.Q(query_object)


class FilterRuleUser(FilterRuleQModel):
    """Filter Rules by User

    Attributes:
        See FilterRuleQModel (includes FilterRuleModel, BaseModel)
        user_id (integer, fk, required): User
    """

    class Meta(FilterRuleModel.Meta):
        db_table = "filter_rule_user"
        verbose_name = "Filter Rule - User"

    filter_rule_user_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,
                             db_column="user_id",
                             related_name="filter_rule_users",
                             null=False, blank=False
                             )

    @property
    def lookup_field(self):
        return "user_id"

    @property
    def lookup_value(self):
        return self.user_id


class FilterRuleGroup(FilterRuleQModel):
    """Filter Rules by Datum Group

    Attributes:
        See FilterRuleQModel (includes FilterRuleModel, BaseModel)
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

    @property
    def lookup_field(self):
        return "datum_type__datum_group_id"

    @property
    def lookup_value(self):
        return self.datum_group_id


class FilterRuleType(FilterRuleQModel):
    """Filter Rules by Datum Type

    Attributes:
        See FilterRuleQModel (includes FilterRuleModel, BaseModel)
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

    @property
    def lookup_field(self):
        return "datum_type_id"

    @property
    def lookup_value(self):
        return self.datum_type_id


class FilterRuleSetModel(FilterRuleModel):
    """Filter rule that outputs datum set

    Attributes:
        See FilterRuleModel (includes BaseModel)
    """

    class Meta(FilterRuleModel.Meta):
        abstract = True

    def get_datum_set(self, datum_filter_rules):
        """Return filter results

        Arguments:
            datum_filter_rules: Collection of filter rule objects
                dictionary of rule lists
                (FilterRuleGroup & FilterRuleType)

        Returns:
            Set of datum_object_ids
        """


class FilterRuleAssociation(FilterRuleSetModel):
    """Filter Rules by Datum Association

    Attributes:
        See FilterRuleSetModel (includes FilterRuleModel, BaseModel)
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

    def get_datum_set(self, datum_filter_rules):

        parent_result = []
        child_result = []

        # Parent Associations
        if self.association_direction == AssociationDirection.parent() or \
                        self.association_direction == AssociationDirection.both():
            # Set datum_filter_rules using parent_datum_id prefix
            parent_datum_filter = compile_Q_objects(datum_filter_rules, "parent_datum")

            parent_result = self.datum_object.association_queryset(
                direction=AssociationDirection.parent(),
                distance_limit=self.distance,
                additional_filter=parent_datum_filter,
                return_method="values_list",
                return_args=["parent_datum__datum_object_id"],
                return_kwargs={"flat": True}
            )

        # Child Associations
        if self.association_direction == AssociationDirection.child() or \
                        self.association_direction == AssociationDirection.both():
            # Set datum_filter_rules using child_datum_id prefix
            child_datum_filter = compile_Q_objects(datum_filter_rules, "child_datum")

            child_result = self.datum_object.association_queryset(
                direction=AssociationDirection.child(),
                distance_limit=self.distance,
                additional_filter=child_datum_filter,
                return_method="values_list",
                return_args=["child_datum__datum_object_id"],
                return_kwargs={"flat": True}
            )

        result = chain(parent_result, child_result, [self.datum_object_id])
        return set(result)


class FilterRuleElement(FilterRuleSetModel):
    """Filter Rules by Element Value

    Attributes:
        See FilterRuleSetModel (includes FilterRuleModel, BaseModel)
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

    def get_datum_set(self, datum_filter_rules):
        datum_object_prefix = "element_datum_object__datum_object"
        element_type_prefix = "element_datum_object__element_type"

        element_value_model = self.element_type.element_value_model
        value_lookup = "elvalue__" + self.operator
        value_query = (value_lookup, self.elvalue)
        type_query = (element_type_prefix + "__element_type_id", self.element_type.element_type_id)
        query = element_value_model.objects.filter(type_query, value_query)

        if datum_filter_rules:
            datum_filter = compile_Q_objects(datum_filter_rules,
                                             datum_object_prefix
                                             )
            query = query.filter(datum_filter)

        result = query.values_list(datum_object_prefix + "__datum_object_id", flat=True)
        return set(result)


class FilterRuleDataType(FilterRuleSetModel):
    """Filter Rules by Data Type

    Apply to entire ElementValue table

    Attributes:
        See FilterRuleSetModel (includes FilterRuleModel, BaseModel)
        element_data_type_id (integer, fk, required): ElementDataType
        elvalue (string):  ***Must match value
    """

    class Meta(FilterRuleModel.Meta):
        db_table = "filter_rule_data_type"
        verbose_name = "Filter Rule - Element Data Type"

    filter_rule_data_type_id = models.AutoField(primary_key=True)
    element_data_type = models.ForeignKey("element_type.ElementDataType",
                                          db_column="element_data_type_id",
                                          related_name="filter_rule_data_types",
                                          null=False, blank=False
                                          )
    elvalue = models.CharField(max_length=255)

    def get_datum_set(self, datum_filter_rules):
        datum_object_prefix = "element_datum_object__datum_object"
        element_type_prefix = "element_datum_object__element_type"

        element_value_model = ElementValueMeta(self.element_data_type.entity_name)
        value_lookup = "elvalue__" + self.operator
        value_query = (value_lookup, self.elvalue)
        query = element_value_model.objects.filter(value_query)

        if datum_filter_rules:
            datum_filter = compile_Q_objects(datum_filter_rules,
                                             datum_object_prefix
                                             )
            query = query.filter(datum_filter)

        result = query.values_list(datum_object_prefix + "__datum_object_id", flat=True)
        return set(result)


class FilterSet(EntityModel):
    """Datum Filters with rules

    Multiple Uses: Views and Associations

    Attributes:
        See EntityModel (includes BaseModel)
        user (integer, fk, optional): User
        rules_dict (dict):
            Lists of FilterSetRule objects related to FilterSet
            Use to run filter
    """

    class Meta(EntityModel.Meta):
        db_table = "filter_set"
        verbose_name = "Filter Set"

    filter_set_id = models.AutoField(primary_key=True)
    # Null user means filter set available to all users??
    user = models.ForeignKey(User,
                             db_column="user_id",
                             related_name="filter_sets",
                             null=True, blank=True
                             )
    filter_rules_user = models.ManyToManyField("filter.FilterRuleUser",
                                                through="filter.FilterSetUserRule",
                                                related_name="+"
                                                )
    filter_rules_group = models.ManyToManyField("filter.FilterRuleGroup",
                                                through="filter.FilterSetGroupRule",
                                                related_name="+"
                                                )
    filter_rules_type = models.ManyToManyField("filter.FilterRuleType",
                                                through="filter.FilterSetTypeRule",
                                                related_name="+"
                                                )
    filter_rules_association = models.ManyToManyField("filter.FilterRuleAssociation",
                                                through="filter.FilterSetAssociationRule",
                                                related_name="+"
                                                )
    filter_rules_element = models.ManyToManyField("filter.FilterRuleElement",
                                                through="filter.FilterSetElementRule",
                                                related_name="+"
                                                )
    filter_rules_data_type = models.ManyToManyField("filter.FilterRuleDataType",
                                                through="filter.FilterSetDataTypeRule",
                                                related_name="+"
                                                )

    @property
    def rules_dict(self):
        rules = {}
        if self.filter_rules_user.exists():
            rules["FilterRuleUser"] = self.filter_rules_user.all()
        if self.filter_rules_group.exists():
            rules["FilterRuleGroup"] = self.filter_rules_group.all()
        if self.filter_rules_type.exists():
            rules["FilterRuleType"] = self.filter_rules_type.all()
        if self.filter_rules_association.exists():
            rules["FilterRuleAssociation"] = self.filter_rules_association.all()
        if self.filter_rules_element.exists():
            rules["FilterRuleElement"] = self.filter_rules_element.all()
        if self.filter_rules_data_type.exists():
            rules["FilterRuleDataType"] = self.filter_rules_data_type.all()
        return rules

    def run_filter(self):
        """Run filter using stored FilterRule objects
        """
        return run_filter_from_model(**self.rules_dict)


class FilterSetUserRule(BaseModel):
    """Assign User Filter Rules to Filter Sets

    Attributes:
        See BaseModel
        filter_set (integer, fk, required): FilterSet
        filter_rule_user_id (integer, fk, required): FilterRuleUser
    """

    class Meta(BaseModel.Meta):
        db_table = "filter_set_user_rule"

    filter_set_user_rule_id = models.AutoField(primary_key=True)
    filter_set = models.ForeignKey("FilterSet",
                                   db_column="filter_set_id",
                                   related_name="filter_set_user_rules",
                                   null=False, blank=False
                                   )
    filter_rule_user = models.ForeignKey("FilterRuleUser",
                                         db_column="filter_rule_user_id",
                                         related_name="filter_set_user_rules",
                                         null=False, blank=False
                                         )


class FilterSetGroupRule(BaseModel):
    """Assign Group Filter Rules to Filter Sets

    Attributes:
        See BaseModel
        filter_set (integer, fk, required): FilterSet
        filter_rule_group_id (integer, fk, required): FilterRuleGroup
    """

    class Meta(BaseModel.Meta):
        db_table = "filter_set_group_rule"

    filter_set_group_rule_id = models.AutoField(primary_key=True)
    filter_set = models.ForeignKey("FilterSet",
                                   db_column="filter_set_id",
                                   related_name="filter_set_group_rules",
                                   null=False, blank=False
                                   )
    filter_rule_group = models.ForeignKey("FilterRuleGroup",
                                          db_column="filter_rule_group_id",
                                          related_name="filter_set_group_rules",
                                          null=False, blank=False
                                          )


class FilterSetTypeRule(BaseModel):
    """Assign Type Filter Rules to Filter Sets

    Attributes:
        See BaseModel
        filter_set (integer, fk, required): FilterSet
        filter_rule_type_id (integer, fk, required): FilterRuleType
    """

    class Meta(BaseModel.Meta):
        db_table = "filter_set_type_rule"

    filter_set_type_rule_id = models.AutoField(primary_key=True)
    filter_set = models.ForeignKey("FilterSet",
                                   db_column="filter_set_id",
                                   related_name="filter_set_type_rules",
                                   null=False, blank=False
                                   )
    filter_rule_type = models.ForeignKey("FilterRuleType",
                                         db_column="filter_rule_type_id",
                                         related_name="filter_set_type_rules",
                                         null=False, blank=False
                                         )


class FilterSetAssociationRule(BaseModel):
    """Assign Association Filter Rules to Filter Sets

    Attributes:
        See BaseModel
        filter_set (integer, fk, required): FilterSet
        filter_rule_association_id (integer, fk, required): FilterRuleAssociation
    """

    class Meta(BaseModel.Meta):
        db_table = "filter_set_association_rule"

    filter_set_association_rule_id = models.AutoField(primary_key=True)
    filter_set = models.ForeignKey("FilterSet",
                                   db_column="filter_set_id",
                                   related_name="filter_set_association_rules",
                                   null=False, blank=False
                                   )
    filter_rule_association = models.ForeignKey("FilterRuleAssociation",
                                                db_column="filter_rule_association_id",
                                                related_name="filter_set_association_rules",
                                                null=False, blank=False
                                                )


class FilterSetElementRule(BaseModel):
    """Assign Element Filter Rules to Filter Sets

    Attributes:
        See BaseModel
        filter_set (integer, fk, required): FilterSet
        filter_rule_element_id (integer, fk, required): FilterRuleElement
    """

    class Meta(BaseModel.Meta):
        db_table = "filter_set_element_rule"

    filter_set_element_rule_id = models.AutoField(primary_key=True)
    filter_set = models.ForeignKey("FilterSet",
                                   db_column="filter_set_id",
                                   related_name="filter_set_element_rules",
                                   null=False, blank=False
                                   )
    filter_rule_element = models.ForeignKey("FilterRuleElement",
                                            db_column="filter_rule_element_id",
                                            related_name="filter_set_element_rules",
                                            null=False, blank=False
                                            )


class FilterSetDataTypeRule(BaseModel):
    """Assign DataType Filter Rules to Filter Sets

    Attributes:
        See BaseModel
        filter_set (integer, fk, required): FilterSet
        filter_rule_data_type_id (integer, fk, required): FilterRuleDataType
    """

    class Meta(BaseModel.Meta):
        db_table = "filter_set_data_type_rule"

    filter_set_data_type_rule_id = models.AutoField(primary_key=True)
    filter_set = models.ForeignKey("FilterSet",
                                   db_column="filter_set_id",
                                   related_name="filter_set_data_type_rules",
                                   null=False, blank=False
                                   )
    filter_rule_data_type = models.ForeignKey("FilterRuleDataType",
                                              db_column="filter_rule_data_type_id",
                                              related_name="filter_set_data_type_rules",
                                              null=False, blank=False
                                              )
