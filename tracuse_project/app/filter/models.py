from django.db import models

from django.contrib.auth.models import User

from app.common.models import EntityModel, BaseModel
from app.association.models import AssociationDirection


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

    operator = models.CharField(max_length=5,
                                default="exact",
                                null=False, blank=False,
                                choices=OPERATOR_CHOICES
                                )
    conditional = models.CharField(max_length=3,
                                   null=True, blank=True,
                                   default="AND",
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

    @property
    def Q_object(self):
        lookup_type = "element_datum_object__datum_object__datum_type__datum_group_id__" + self.operator
        query_object = (lookup_type, self.datum_group_id)
        return models.Q(query_object)


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

    @property
    def Q_object(self):
        lookup_type = "element_datum_object__datum_object__datum_type_id__" + self.operator
        query_object = (lookup_type, self.datum_type_id)
        return models.Q(query_object)


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

    def get_datum_set(self, datum_property_query):

        from itertools import chain

        if self.association_direction == AssociationDirection.parent() or \
                        self.association_direction == AssociationDirection.both():
            parent_result = self.datum_object.association_queryset(
                direction=AssociationDirection.parent(),
                distance_limit=self.distance,
                return_method="values_list",
                return_args=["parent_datum__datum_object_id"],
                return_kwargs={"flat": True}
            )

        if self.association_direction == AssociationDirection.child() or \
                        self.association_direction == AssociationDirection.both():
            child_result = self.datum_object.association_queryset(
                direction=AssociationDirection.child(),
                distance_limit=self.distance,
                return_method="values_list",
                return_args=["child_datum__datum_object_id"],
                return_kwargs={"flat": True}
            )

        result = chain(parent_result, child_result)
        return set(result)


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

    def get_datum_set(self, datum_property_query):
        element_value_model = self.element_type.element_value_model
        value_lookup = "elvalue__" + self.operator
        value_query = (value_lookup, self.elvalue)
        type_query = ("element_datum_object__element_type_id", self.element_type.element_type_id)
        query = element_value_model.objects.filter(type_query, value_query)

        if datum_property_query:
            query = query.filter(datum_property_query)

        result = query.values_list("element_datum_object__datum_object_id", flat=True)
        return set(result)


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
    user = models.ForeignKey(User,
                             db_column="user_id",
                             related_name="filter_sets",
                             null=True, blank=True
                             )

    @classmethod
    def _compile_Q_rules(cls, filter_rules):
        """Compile filter rules using Q objects and conditionals

        Arguments:
            filter_rules: Filter rule objects that output query objects
                (FilterRuleGroup & FilterRuleType)

        Return:
            Q object
        """
        output = models.Q()

        first_rule = True
        for filter_rule in filter_rules:
            Q_object = filter_rule.Q_object
            if first_rule:
                output = Q_object
                first_rule = False
            else:
                output.add(Q_object, filter_rule.conditional)

        return output

    def _compile_datum_set_rules(self, filter_rules, datum_property_query):
        """Compile filter rules using datum set and conditionals

        Arguments:
            filter_rules: Filter rule objects that output datum sets
                (FilterRuleAssociation & FilterRuleElement)
            datum_property_query: filter on datum_object properties
                (datum_group & datum_type)

        Return:
            Set of datum_object_ids
        """
        output = set()

        first_rule = True
        for filter_rule in filter_rules:
            datum_set = filter_rule.get_datum_set(datum_property_query)
            if first_rule:
                output = datum_set
                first_rule = False
            else:
                if filter_rule.conditional == "AND":
                    output = output.intersection(datum_set)
                else:
                    output = output.union(datum_set)

        return output

    def _run_filter_set(self, **kwargs):
        """Apply filter rules and return list of datum_object_ids

        Arguments:
            group_rules (list): FilterRuleGroup instances
            type_rules (list): FilterRuleType instances
            association_rules (list): FilterRuleAssociation instances
            element_rules (list): FilterRuleElement instances

        Returns:
            List of datum_object_ids
        """
        output = set()

        # Compile group rules with conditionals
        group_Q = models.Q()
        if "group_rules" in kwargs:
            group_Q = self._compile_Q_rules(kwargs["group_rules"])

        # Compile type rules with conditionals
        type_Q = models.Q()
        if "type_rules" in kwargs:
            type_Q = self._compile_Q_rules(kwargs["type_rules"])

        # Create datum_property_query to pass to association and element rules
        datum_property_query = models.Q(group_Q & type_Q)

        # Compile association rules with conditionals
        association_set = ()
        if "association_rules" in kwargs:
            association_set = self._compile_datum_set_rules(
                filter_rules=kwargs["association_rules"],
                datum_property_query=datum_property_query
            )

        # Compile element rules with conditionals
        element_set = ()
        if "element_rules" in kwargs:
            element_set = self._compile_datum_set_rules(
                filter_rules=kwargs["element_rules"],
                datum_property_query=datum_property_query
            )

        output = association_set & element_set

        return output


class FilterSetRuleModel(BaseModel):
    """Common properties for assigning Filter Rules to Filter Sets

    Includes rule ordering

    Attributes:
        See BaseModel
        filter_set_id (integer, fk, required): FilterSet
    """

    class Meta(BaseModel.Meta):
        abstract = True

        # filter_set_id defined in each model due to
        # foreign key related names not being inherited


class FilterSetGroupRule(FilterSetRuleModel):
    """Assign Group Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleModel (includes Base)
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


class FilterSetTypeRule(FilterSetRuleModel):
    """Assign Type Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleModel (includes Base)
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


class FilterSetAssociationRule(FilterSetRuleModel):
    """Assign Association Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleModel (includes Base)
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


class FilterSetElementRule(FilterSetRuleModel):
    """Assign Element Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleModel (includes Base)
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
